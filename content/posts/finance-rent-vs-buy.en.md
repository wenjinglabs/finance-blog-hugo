---
title: "Rent vs Buy: The Break-Even Math, With Real Numbers"
description: "\"Renting is throwing money away\" and \"buying is a trap\" are both slogans. I modeled the same $400k house against renting and investing the difference — here is exactly where the break-even sits."
slug: finance-rent-vs-buy
date: "2026-10-25"
tags: [Personal Finance, Housing]
---
cover:
  src: /images/kimitachi005.avif
  alt: cover

{{< summary >}}
- In the base model (3% appreciation, 6% investment return), buying and renting are within a few thousand dollars for 20+ years.
- Buying clearly wins when appreciation beats your investment return by ~2.6%/yr of carrying costs; below that, renting + investing wins.
{{< /summary >}}

No personal-finance debate is louder than rent vs buy, and almost nobody argues with numbers. "Renting is throwing money away." "Buying locks you into a trap." Both are slogans. So I built a full model of a concrete scenario and ran it across different holding periods and market conditions. The result is more interesting than either slogan: **buying and renting are closer to a tie than either camp admits — and the whole fight reduces to two numbers: home appreciation vs your investment return.**


## The scenario

| Parameter | Buy | Rent |
|---|---|---|
| Home price | $400,000 | — |
| Monthly rent | — | $2,000 (+3%/yr) |
| Upfront cost | $92,000 (20% down + 3% closing) | $0 |
| Mortgage | $320,000 @ 6%, 30-yr fixed (P&I ≈ $1,919) | — |
| Carrying costs | 1.2% tax + 1% maintenance + 0.4% insurance ≈ $867/mo | included in rent |
| Growth | home appreciation: varied below | invested difference at 6%/yr |
| Exit friction | 7% of sale price (agent + transfer) | none |

The renter invests the $92,000 upfront **and** the monthly difference between the owner's total cost ($2,785) and their rent — that's the fair comparison, and it's the one most rent-vs-buy takes skip. Price-to-rent ratio here: $400,000 ÷ ($2,000 × 12) = **16.7**. (Below ~15 generally leans buy; above ~20 leans rent.) Local appreciation history lives in official indexes like the [FHFA House Price Index](https://www.fhfa.gov/data/hpi).


## The break-even table

Net-worth difference between buying and renting (positive = buying wins), by annual home appreciation and holding period, with investments returning 6%/yr:

| Home appreciation | After 10 yrs | After 20 yrs | After 30 yrs |
|---|---|---|---|
| 2%/yr | -$56k | -$95k | -$212k |
| 3%/yr | -$16k | -$3k | -$32k |
| 4%/yr | +$28k | +$99k | +$187k |
| 5%/yr | +$76k | +$221k | +$408k |
| 6%/yr | +$129k | +$372k | +$715k |

Read that middle row again: **at 3% appreciation — roughly the long-run US average — the two strategies are statistically indistinguishable for two decades.** The decision only becomes big when appreciation is clearly above or below your investment return. And with a conservative 4% investment return instead, buying wins at just 3% appreciation (worth +$151k at 20 years). The relationship that matters:

> Buying wins when home appreciation beats your investment return by roughly the ~2.6%/yr carrying cost and the 7% exit friction. Everything else — the forced savings, the pride, the landlord stories — is commentary.


## Why renting isn't "throwing money away"

- **Rent buys shelter, exactly like a mortgage buys shelter.** The owner's version of \"throwing money away\" is the $867/mo of tax, maintenance, and insurance — money that buys no equity at all. In year one of our model, the owner pays about $14,500 in interest (also no equity) plus that carrying cost.
- **The renter in this model ends up with a real portfolio** — around $514k after 20 years at 6%. \"Rent money disappears\" only if the difference actually disappears instead of being invested. It usually doesn't, and that's a behavior risk, not a math one.
- **Leverage cuts both ways.** The owner controls a $400k asset with $92k — wonderful at 5% appreciation, brutal at 2%. The renter's exposure is never leveraged.


## What the model deliberately ignores

- **Flexibility.** Renting keeps you mobile for a job change or family change — worth real money that depends entirely on your life. Buying a home with a 30-year loan and selling in year 3 eats the friction twice.
- **Taxes and subsidies.** Deductions, first-time-buyer programs, and local rules shift the math by country and by person. None are in the model.
- **Rent-control regimes and insurance-less medical events** — the model assumes smooth 3% rent growth; many cities are not smooth.


## The decision rule I'd actually use

1. **Stability first.** If you might move within ~5 years, renting wins almost regardless of the market — the 7% friction on a $400k home is $28,000 before any appreciation helps you.

One more honesty note: every number above is a parameter you can argue with — 6% investment returns, 3% appreciation, 1% maintenance. The conclusion isn't any single row; it's the shape: **the rent-vs-buy fight is mostly a fight about two rates, and you can look up both for your own city before you decide.**

