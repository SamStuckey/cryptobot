# Cryptobot-V1

## TDD

## Goal: 
  ensure 1% per day gain

### Schema

|----------------|-----|--------------------------------------------|
| Order          |     |                                            |
|----------------|-----|--------------------------------------------|
| purchase_price | int | set by transaction                         |
| sell_threshold | int | set via service that calculates difference |


### Bellows Pattern


- When to buy
  - set a starting point (S)
  - set an interval      (X)
  - set a quantity       (Q)
  - set a gain threshold (T)
  - record buy-at price  (P) per order

# brainstorm
if we drop below a threshold by our margiin
  - start at 100 bucks per coin
  - if it goes to $90, buy $10 worth
    - loose 10
  - if it goes to $80 buy $10 worth
    - loose 10
  - if it goes to $70 buy $10 worth
    - loose 10

  - goes up to 80, sell my $70 shares
    + make 10
  - goes down to 70 buy 10
    - loose 10
  - goes up to 80 sell 70 shares
    + make 10
  - goes up to 90 sell 80 shares
    + make 10

- Kick up to 15 
  - currently -10 bucks 
  - currently @ 90
  - currently own 10 worth at 90
  - goes down to 80 buy 15
    - loose 15
  - goes down to 70 buy 15
    - get 15
  - goes up to 90
    + get 15
  - goes up to 100
    + get 15
    + get 10



  

1. Recognize trends
  - candles
    - buy on 
      - bullish hammer reversal
      - bullish engulfing candel
    - sell onn
      - bearish engulfing candel
      - bearish hammer reversal
  - 1% patternn
  - bellows pattern 
