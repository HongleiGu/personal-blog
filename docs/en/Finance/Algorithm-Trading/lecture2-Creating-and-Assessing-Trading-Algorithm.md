
# Trading Algorithm

Input (Historical and Live data) -\> Decision Making(Strategy) -\>
Output(Traidng signal)

when we meet some certain signals, we trade

## Moving average/momentum

Using the moving averages to identify the direction/momentum of a stock

Involves takeing the average stock price over fast and slow period
usually 50-day and 200-day

[\\(SMA = \\frac{A_1 + A_2+\\dots + A_n}{n}, A_n = \\text{asset price at
period n}, n = \\text{total number of periods}\\)]{.arithmatex}

if the fast cross the slow

- fast over slow: upward, a buy signal (bullish)
- slow over fast: downward, a sell signal (bearish)

## long and short positions

on a long position on a stock means buying th e stock with the
expectation that the price will rise

short otherwise

Ma seems to be a bit short

so

![slide31](../../../assets/Finance/lecture2-slide31.png)

## weighted moving average

more recent periods have higher weights, thus greater influence in the
average

[\\(WMA = \\frac{\\sum\_{i=1}\^n w_ix_i}{\\sum\_{i=1}\^n
w_i}\\)]{.arithmatex}

[\\(\\begin{aligned} x_i &= \\text{value of asset at ith period}\\\\ w_i
&= \\text{weight of asset at ith period}\\\\ n &= \\text{total number of
assset}\\\\ i &= \\text{sum of all weights}
\\end{aligned}\\)]{.arithmatex}

even more responsive

## Exponetial Moving average

[\\(EMA_t = Price(t) \* k + EMA\_{t-1}\\times (1-k)\\)]{.arithmatex}

[\\(\\begin{aligned} t &= \\text{today}\\\\ n &= \\text{number of
days}\\\\ k &= \\text{smoothing factor}\\frac{2}{1+n}
\\end{aligned}\\)]{.arithmatex}

EMA is more sensitive helping to identify trends earlier

but does experience more sudden short-term changes

# Mean reversion

assume that hte asset prices wil retunr ot the histroical average, or
mean, after deviating from it.

## concepts

- natually fluctuate
- efficient market hypothesis
- investor behavior biases

(Investors overreact to merket news etc, A stock\'s price is reflective
of all information)

## how it works

rolling averages to determine the mean price

set bounds, if the flucuation went beyond the bounds, we enter a trade

if the price reverts to its historical average, we profit

## bounds and limits

### z-score

how much standard deviations it is from the mean

if its below the mean, its short

[\\(Z = \\frac{P - \\mu}{\\sigma}\\)]{.arithmatex}

### bolliger bands

- Upper band: 20-day SMA + (20-day standard deviation \* 2)
- Middle band: 20-day SMA
- Lower band: 20-day SMA - (20-day standard deviation \* 2)

### RSI(reletive strength index)

[\\(\\begin{aligned} RSI &= 100 - (\\frac{100}{1+RS})\\\\ RS &=
\\frac{\\text{Average of x days\' up closes}}{\\text{Average of x days\'
down closes}} \\end{aligned}\\)]{.arithmatex}

# pair trading

monitor the price divergence of two highly correlated assets

The price difference is referred to as the spread and when the spread
diverges (greater than set bounds) it presents a trading opportunity

Long the undervalued assest and short the overvalued, and close both
trades once they revert

use Z-scores or standard deviation to set bounds for the spread

## Monitor spread

We calculate spread of asset via a ratio of their prices

[\\(\\begin{aligned} \\text{Spread} &= \\frac{P_A}{P_B}\\\\ P_x &=
\\text{price of asset x} \\end{aligned}\\)]{.arithmatex}

# drawdown

the peak-to-trough decline during a specific period for an investment

- maximum drawdown: The largest drop from a peak to a trough over the
  trading period
- Relative Drawdown: Percentage decline from the highest equity point
  relative to the account balance

high drawdown is caused by high volatility

# measure volatility

- Standard deviation: widely regarded as a highly effective measure of
  volatility - it quantifies how much return deviate from the average
- Higher standard deviation implies more variability(volatility) in
  returns, while a lower standard deviation indicates returns are closer
  to the average, suggesting less volatility

## Sharpe Ratio

[\\(S = \\frac{R_p - R_f}{\\sigma_p}\\)]{.arithmatex}

[\\(\\begin{aligned} R_p &= \\text{Expect return(or actual return) of
portfolio/investment}\\\\ R_f &= \\text{Risk-free rate(e.g. return of
government bonds)}\\\\ \\sigma_p &= Standard deviation of the
portfolio\'s returns (a measure of risk or volatility)
\\end{aligned}\\)]{.arithmatex}

the amount of return per risk
::::
::::::::::::::
:::::::::::::::
