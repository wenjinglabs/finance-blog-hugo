---
title: "Lump Sum vs Dollar-Cost Averaging: 155 Years of Data, Every Starting Month"
description: "You have $100,000 to invest. All at once, or spread over 12 months? I ran every starting month since 1871 through real S&P 500 total-return data — here are the win rates, the worst cases, and the price of each strategy's insurance."
slug: finance-lump-sum-vs-dca
date: "2026-10-25"
tags: [Investing, Index Funds]
---
cover:
  image: /images/laputa030.avif
  alt: cover
  relative: false

A bonus, an inheritance, a home sale — one day you're holding a large sum and facing the most uncomfortable question in personal finance: **invest it all today, or spread it out?** Spreading feels safer. Investing everything at once feels reckless. I wanted actual numbers rather than feelings, so I ran a backtest on 155 years of real market data — every possible starting month from 1871 through September 2026, using Robert Shiller's [publicly available S&P 500 dataset](https://shillerdata.com/) with dividends reinvested.


## The setup, stated plainly so you can attack it

- **Lump sum (LS):** invest the full $100,000 on day one.
- **DCA-12:** split it into 12 equal monthly installments; uninvested cash sits idle (earning nothing — deliberately conservative).
- **Measurement:** compare final values 12 months after the start date. Every starting month from the dataset is a separate trial.
- **Returns:** total return — price change plus dividends reinvested monthly.

This mirrors the methodology of Vanguard's [cost-averaging research paper](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf), which found lump sum winning roughly two-thirds of the time in US data. My numbers came out a bit stronger — because a 100% equity index is more volatile (and drifts upward more reliably) than their 60/40 portfolios.


## Result one: lump sum wins about 3 times out of 4

| Period | LS win rate | LS average advantage | Median advantage | LS worst case |
|---|---|---|---|---|
| Since 1950 (909 trials) | **77.3%** | +5.2% | +5.8% | -28.1% (start: May 2008) |
| Since 1871 (1,857 trials) | 72.0% | +4.3% | +4.6% | -42.5% (start: Aug 1931) |

Three observations worth more than the table. **First, the horizon doesn't matter** — win rates are nearly identical at 12, 24, 36, 60, and 120 months, because both strategies hold the market after month 12; the decision only concerns the first year. **Second, the average cost of a 12-month DCA is about 5%.** That is the expected price of spreading out. **Third, the worst case is exactly what you'd guess: deploying everything into May 2008**, two-thirds of the way into the financial crisis. The lump-sum investor was down 28% relative to a co-worker who spread the same money over the year.


## Result two: the five worst times to invest everything

Win rates hide the tails, so here are the famous crash eves — what actually happened to a $100,000 lump sum versus a 12-month DCA, measured 12 months later:

| Starting month | Lump sum after 12 mo | DCA-12 after 12 mo | DCA's advantage |
|---|---|---|---|
| Sep 1929 (Great Depression) | $69k | $92k | +32% |
| Aug 1987 (Black Monday) | $83k | $100k | +21% |
| Oct 2007 (financial crisis) | $64k | $72k | +12% |
| Dec 2021 (rate-shock bear) | $85k | $95k | +12% |
| Mar 2000 (dot-com peak) | $83k | $85k | +2% |

This is DCA's entire case, stated honestly: **in the worst 5-10% of starting months, spreading out saves you somewhere between 2% and 32% of the principal.** In the other 90%+, it quietly costs you an average of 5%. You are not choosing between smart and stupid. You are choosing whether to buy insurance against bad timing, and what premium you're willing to pay for it.


## Result three: the insurance price list

If you've decided to spread out — or you know you'll panic — the length of the schedule is a dial you control. Since 1950, evaluated 12 months after start:

| Strategy | Beats lump sum | Average cost vs LS | Worst case vs LS |
|---|---|---|---|
| 3-month schedule | 31.6% of the time | -0.8% | -9.6% |
| 6-month schedule | 26.3% of the time | -2.0% | -16.4% |
| 12-month schedule | 22.7% of the time | -4.3% | -24.8% |

The 3-month schedule is the sleeper result here: **it keeps most of DCA's psychological comfort while giving up less than 1% of expected return.** The classic 12-month schedule, by contrast, pays the full insurance premium. Most people never consider that the schedule length is a choice — they default to 12 months because that's how the term "dollar-cost averaging" is usually described.


## The part statistics can't decide: regret

On paper this post ends here: lump sum wins 77% of the time, invest and go. But money is felt, not modeled, and the two strategies fail in asymmetric ways. The lump-sum investor who deploys at a crash eve watches their new portfolio drop 30% and knows it was **their single decision**. The DCA investor who watches the market rip upward during their schedule suffers a slow, recurring regret — and research and lived experience suggest the second pain is easier to survive than the first. That asymmetry is real, it's psychological rather than mathematical, and pretending it away produces investors who abandon plans. A plan you can actually hold through its worst moment beats the optimal plan you quit — the same logic that makes interruption the enemy in [compound growth](/posts/finance-compound).

There is also a second behavioral trap, and it's the more dangerous one: **DCA plans don't fail at the math, they fail at completion.** Twelve months is twelve separate decisions to buy, each one an opportunity to "wait until things settle." The backtest above assumes flawless execution. If you honestly doubt you'll finish the schedule, the automatic, immediate, boring lump sum is the safer choice **for you**, regardless of what the win rate says. And if the money is sitting in a 0.2% checking account "temporarily," the drag is identical to the one that makes idle cash a [guaranteed real loss](/posts/finance-compound).


## The decision rules I'd actually use



Honest limitations, in one breath: this is US large-cap data only; dividends were reinvested but taxes were not modeled; idle DCA cash earned zero rather than treasury rates (crediting it would narrow the gap by roughly a third); and 155 years of one country's rising market is the only history we get — [equity drawdowns](/posts/finance-nasdaq-drawdown) in other markets have taken decades, not years. The data narrows the decision; it cannot make it for you.

> Lump sum wins three times out of four and costs you nothing but nerve. DCA is insurance: know the premium, choose the deductible, set the schedule before the money lands — then stop renegotiating with yourself.

