
# Impact:

the effect that a market participant has on the price of an asset when
it buys or sells that asset

say, if I buy 1M worth of shares, what will happen to the market.

## The Order Book:

![slide4](../../../assets/Finance/lecture5-slide4.png)

A bid-ask spread is the difference between the highest price that a
buyer is willing to pay for an asset and the lowest price that a seller
is willing to accept.

In the example above:

- the mid price is 100, it is the average of the highest bid price and
  the lowest ask price
- the Last traded price is not provided, but should be somewhere in the
  range, typically a order book is in pairs, with the lastest one in the
  top
- the Volume Weight Average Price is the weighted average of the bid and
  ask repectively

so [\\(VWAP\_{Bid} = {96\\times 100 + 97\\times 50 + 98 \\times 150 +
99\\times 100}{100 + 50 + 150 + 100} = 97.625\\)]{.arithmatex}

similar for sell/ask

Market Events: - if I want to buy 200 shares, I should look at the sell
section, I may wait of an approprate price - if I want to sell, I should
look at the buy section - if I need to buy immediately, then I need to
pick the 200 share \$101 option

![slide8](../../../assets/Finance/lecture5-slide8.png)

so before there was this 200 shares, \$101 row, now it is purchased

the number are almost identical, but that is not a association between
limit order and market order

a limit order is just an buying requirement, say I need to wait until
the stock price is \$10 and buy

## Price change

then after removing the 200 share \$101, the new mid-price is 101

any purchase that is not the highest bid or lowest ask does no effect to
the mid price

## other book events:

- stop order
- stop limit order
- order cancelation
- fill-or-kill order
- immediate or cancel order
- good-till-cancelled

# Meta-Orders

conside the same scenario, I need to buy 400 or more shares

- it is not possible since all the sell order adds up to only 210
- is there enough liquidity, not

Meta-orders is used to trade in large amounts

Meta orders is the ensemble of all trades, executed incrementally that
belong to one single trading decision

the execution strategies can be complex to minimize market impact

The insight from Meta-orders over single-orders gives us insight about
the liquidity needs and market impact

![slide15](../../../assets/Finance/lecture5-slide15.png)

## Consequences of Meta-orders:

Most trades belong to some meta-order

so buys tend to follow by buys, and sells tend to follow by sells

# Impact

## Types of Impact

We looked at informational impact in the limit order example, which is
the long-term price

In the market order example, we looked at mechanical impact - the short
term price change

### Mechanical impact:

the Immediate and exact changes

for example, our bid has increased the prices, causing a short term
effect on the price, bu this impact relaxes, drifts back to the original
mid-price relatively quickly

### Informational Impact

Underpins the momentum of a stock

if we have many buy orders in succession, this implies the asset is
undervalued

This has a long-term effect

for example, other investors see me purchasing this asset so they
purchase this as well, this causes a price increase

### Observed Impact

The mechanical impact of non-random orders as part of a meta-order is
not zero

The total impact, both machenical and informational is hard to model

#### example:

I want to buy 1000 shares of Asset A:

- the initial price was \$2
- we expect total cost to be \$2000
- Actually buying 1000 shares cost \$2300 due to price increases during
  purchase
- we lost \$300 to impact

## Model Impact:

- A good modal allows us to make better informed decisions about whether
  we want to invest in an asset

- In the previous example, if we knew we would lose \$300 to impact, we
  may not have executed

### A basic model:

- Mechanical impact causes high initial price deviation
- Informational impact causes tend to permanent impact

[\\(\\Delta p(t) = \\Delta p\_{perm} + \\Delta p\_{overshoot}\\bullet
e\^{-\\alpha t} - \\Delta p\_{overshoot}\\bullet e\^{-\\beta
t}\\)]{.arithmatex}

[\\(\\Delta p\_{perm}\\)]{.arithmatex} is informational impact,
[\\(\\Delta p\_{overshoot}\\)]{.arithmatex} is Mechanical impact, and
[\\(e\^{something}\\)]{.arithmatex} is Exponential Decay

can be something like this

![slide29](../../../assets/Finance/lecture5-slide29.png)

## strategies:

### VWAP Strategy:

The key Idea is to Match the execution price of the order as closely as
possible to the market\'s VWAP over a period

Strategy:

- Split your order into small chunks
- Place orders in proportion to the trading volume at the time
- Heavier weights during high-volume periods reduces impact

![slide32](../../../assets/Finance/lecture5-slide32.png)

### TWAP Strategy:

The key Idea is the execute at regular intervals uniformly over a period

Strategy:

- Split the order into small chunks
- Place equally weighted orders at equal intervals over time
- this is simpler than VWAP
- better in illiquid markets when volume is unpredictable

# Dark Pools:

What effect does the hiding of limit orders have on impact?

- Trades are matched internally with a number of different mechanisms
- Prices may still be affected due to post-trade reporting and signaling
- Usually used by large scale investors to hide impact
::::
::::::::::::::
:::::::::::::::
