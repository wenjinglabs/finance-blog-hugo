"""
把 Next.js 博客的 TS 文章内容转换成 Hugo 双语 markdown。
- 每篇文章生成 content/posts/<slug>.en.md 和 <slug>.zh.md（Hugo multilingual 约定）
- blocks: p/h2/h3/ul/ol/quote/table/summary/chart/img
- chart 块转成 {{< chart ... >}} shortcode（服务端渲染 SVG）
- img 块转成 {{< figure ... >}} shortcode
- links 保留 markdown 语法
"""
import io
import os
import re
import json

SRC = r"C:\Users\35425\WorkBuddy\2026-10-23-23-51-18\meme-blog-next\src\content"
OUT = r"C:\Users\35425\WorkBuddy\finance-blog-hugo\content\posts"
STATIC_IMG = r"C:\Users\35425\WorkBuddy\finance-blog-hugo\static\images"

os.makedirs(OUT, exist_ok=True)
os.makedirs(STATIC_IMG, exist_ok=True)

def parse_blocks(text):
    """极简 TS 数组解析: 逐块匹配 { t: "xxx", ... }"""
    blocks = []
    # 用平衡括号扫描
    i = 0
    n = len(text)
    while i < n:
        m = re.search(r'\{\s*t:\s*"(p|h2|h3|ul|ol|quote|table|summary|chart|img)"', text[i:], re.S)
        if not m:
            break
        start = i + m.start()
        # 找配对右括号
        depth = 0
        j = start
        while j < n:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        blocks.append(text[start : j + 1])
        i = j + 1
    return blocks


def get_str(block, key):
    m = re.search(key + r':\s*"((?:[^"\\]|\\.)*)"', block, re.S)
    if not m:
        return None
    return m.group(1).replace('\\"', '"').replace("\\\\", "\\")


def get_str_array(block, key):
    m = re.search(key + r":\s*\[(.*?)\]", block, re.S)
    if not m:
        return []
    return re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1))


def get_num_array(block, key):
    m = re.search(key + r":\s*\[(.*?)\]", block, re.S)
    if not m:
        return []
    return [float(x) for x in re.findall(r"-?[\d.]+", m.group(1))]


def esc_md(s):
    return s  # markdown 保留


def block_to_md(b):
    t = get_str(b, "t") or re.search(r't:\s*"([a-z0-9]+)"', b).group(1)
    if t in ("p", "h2", "h3", "quote"):
        text = get_str(b, "text")
        if text is None:
            return ""
        text = text.replace("**", "**")  # keep
        if t == "p":
            return esc_md(text) + "\n"
        if t == "h2":
            return "\n## " + esc_md(text) + "\n"
        if t == "h3":
            return "\n### " + esc_md(text) + "\n"
        return "> " + esc_md(text) + "\n"
    if t in ("ul", "ol", "summary"):
        items = get_str_array(b, "items")
        lines = []
        for i, it in enumerate(items):
            prefix = "1. " if t == "ol" else "- "
            lines.append(prefix + esc_md(it))
        body = "\n".join(lines) + "\n"
        if t == "summary":
            body = "{{< summary >}}\n" + body + "{{< /summary >}}\n"
        return body
    if t == "table":
        head = get_str_array(b, "head")
        rows_m = re.search(r"rows:\s*\[(.*?)\]\s*,?\s*\}", b, re.S)
        rows = []
        if rows_m:
            for rm in re.findall(r"\[((?:[^\[\]]|\\.)*)\]", rows_m.group(1)):
                rows.append(re.findall(r'"((?:[^"\\]|\\.)*)"', rm))
        lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
        for r in rows:
            lines.append("| " + " | ".join(r) + " |")
        return "\n".join(lines) + "\n"
    if t == "chart":
        # shortcode: {{< chart type title labels values unit highlight >}}
        ctype = get_str(b, "type") or "hbar"
        title = get_str(b, "title") or ""
        labels = get_str_array(b, "labels")
        values = get_num_array(b, "values")
        unit = get_str(b, "unit") or ""
        hi_m = re.search(r"highlight:\s*(\d+)", b)
        hi = hi_m.group(1) if hi_m else ""
        return (
            '{{< chart type="%s" title="%s" labels="%s" values="%s" unit="%s" highlight="%s" >}}'
            % (
                ctype,
                title.replace('"', "'"),
                ";".join(labels).replace('"', "'"),
                ";".join(str(int(v)) if v == int(v) else str(v) for v in values),
                unit,
                hi,
            )
        ) + "\n"
    if t == "img":
        src = get_str(b, "src") or ""
        alt = get_str(b, "alt") or ""
        alt_zh = get_str(b, "altZh") or alt
        cap = get_str(b, "caption") or ""
        cap_zh = get_str(b, "captionZh") or cap
        accent = get_str(b, "accent") or ""
        return (
            '{{< figure src="%s" alt="%s" altZh="%s" caption="%s" captionZh="%s" accent="%s" >}}'
            % (src, alt.replace('"', "'"), alt_zh.replace('"', "'"), cap.replace('"', "'"), cap_zh.replace('"', "'"), accent)
        ) + "\n"
    return ""


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


# ---------- 遍历文章文件 ----------
post_files = [f for f in os.listdir(SRC) if f.startswith("finance-") and f.endswith(".ts")]
converted = []
for fname in sorted(post_files):
    src = io.open(os.path.join(SRC, fname), encoding="utf-8").read()
    slug_m = re.search(r'slug:\s*"([^"]+)"', src)
    slug = slug_m.group(1)
    date_m = re.search(r'date:\s*"([^"]+)"', src)
    date = date_m.group(1)[:10]

    # 主（英文）块
    main_m = re.search(r"blocks:\s*\[(.*?)\n  \],\n  zh:", src, re.S) or re.search(r"blocks:\s*\[(.*?)\n  \],\n\};", src, re.S)
    en_blocks = parse_blocks(main_m.group(1))
    en_title = get_str(src, "title")
    en_desc = get_str(src, "description")
    en_tags = get_str_array(src.split("zh:")[0], "tags")

    # zh 块
    zh_m = re.search(r"zh:\s*\{(.*?)\};\s*$", src, re.S)
    zh_title = zh_desc = None
    zh_tags, zh_blocks = [], []
    if zh_m:
        zh_src = zh_m.group(1)
        t_m = re.search(r'title:\s*"((?:[^"\\]|\\.)*)"', zh_src)
        zh_title = t_m.group(1).replace('\\"', '"') if t_m else None
        d_m = re.search(r'description:\s*"((?:[^"\\]|\\.)*)"', zh_src)
        zh_desc = d_m.group(1).replace('\\"', '"') if d_m else None
        zh_tags = get_str_array(zh_src, "tags")
        zb_m = re.search(r"blocks:\s*\[(.*?)\]\s*,?\s*\}\s*$", zh_src, re.S) or re.search(r"blocks:\s*\[(.*)\]", zh_src, re.S)
        if zb_m:
            zh_blocks = parse_blocks(zb_m.group(1))

    cover_m = re.search(r"^\s*img:\s*\{", src, re.M)

    # en md
    en_body = "\n".join(block_to_md(b) for b in en_blocks)
    en_fm = [
        "---",
        f"title: {yaml_str(en_title)}",
        f"description: {yaml_str(en_desc)}",
        f"date: {yaml_str(date)}",
        "tags: [" + ", ".join(en_tags) + "]",
        "---",
        "",
    ]
    io.open(os.path.join(OUT, slug + ".en.md"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(en_fm) + "\n" + en_body + "\n"
    )

    # zh md
    if zh_title and zh_blocks:
        zh_body = "\n".join(block_to_md(b) for b in zh_blocks)
        zh_fm = [
            "---",
            f"title: {yaml_str(zh_title)}",
            f"description: {yaml_str(zh_desc)}",
            f"date: {yaml_str(date)}",
            "tags: [" + ", ".join(zh_tags) + "]",
            "---",
            "",
        ]
        io.open(os.path.join(OUT, slug + ".zh.md"), "w", encoding="utf-8", newline="\n").write(
            "\n".join(zh_fm) + "\n" + zh_body + "\n"
        )

    converted.append((slug, bool(zh_title)))
    print(slug, "en ok, zh:", bool(zh_title and zh_blocks))

print(f"\n{len(converted)} posts converted")
