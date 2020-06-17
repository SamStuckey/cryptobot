# Cryptobot-V1

## TDD

## Goal: 
  ensure 1% per day gain

### Object structure

# Bellows
- set threshold (e.g.
- set buy order 10 below
main program
  It buys bitcoin and records the price it was bought at, then sells it again at it's resale price
  - populate wallet
    - how do i pull from a coinbase (or similar) exchange wallet?
  - buy bitcoin
    - Bellows Schema
      - connect wallet
        - Problem: fees are higher from USD to BTC thann inter-coin trades
          - Solution: Fiat wallet? 
            - I thikn this is an exchannge specific interem wallet
              - Problem: subject to government backinng, can cause hyperinflationn
          - Solution: Exchange wallet?
            - coinbase wallet
        - Problem: 
      - set up tracking database
        - Track trades
        - track exchange rates?
      - set up real time data
        - I cann manage queryinng on my applicationn end
        - or i can pay for the websockets subscriptionn




### Schema

|----------------|-----|--------------------------------------------|
| Order          |     |                                            |
|----------------|-----|--------------------------------------------|
| purchase_price | int | set by transaction                         |
| sell_threshold | int | set via service that calculates difference |


| Exchange |  |
|----------|--|
| symbol   |  |

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
