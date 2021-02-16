# Cryptobot

This is a WIP algorytmic trading bot.  It's purpouse is for it's author to learn
python.

## DO NOT USE THIS WITH REAL MONEY
I mean you can... I do.. but this was built by an engineer for engineery reasons,
and the algorithm(s) herein are not to be taken as sound financial strategies.

## TODO:
- Refactor out redundant methodsf
  - `refresh_foo` should become `foo(refresh=False)`
  - remove duplicates and kruft
- Complete first refactor out of monolith
    The first version of Cryptobot was essentiallly a 'hello world'.  now that I've
    got it working, I'm updating it to have distinct models for 
      - coins
      - bank 
      - transactor
      - algorithms
      - whatever else I come up with along the way

- Add setup.py
    Handle the dependencies for the app and Cbpro2

- figure out a sustainable alternative to CBpro2
    This is a quick fork of CBPro.  The reason it is included in this project
    is simplly because CBPro doesn't return headers from it's API calls.  I should
    probably submit a PR to the CBPro project to tweak this so i don't have to
    maintain this library on my own.

- update trend reversal logic to use velocity or buy / sell ratio
    I can make this way smarter by watching for shifts in market trends
    instead of hard numbers.  I think this will work best for buying, as it
    can indicate the approach of a floor.  
    However, it's a little fuzzier on sales, as we want to avoid false positives.
    Maybe set up a more refined sale trigger that watches for both percentange
    changes and downticks, in conjunction with a hard stop loss below peaks.

## Coinbase API response models
### MARKET BUY RESPONSE 
```
{
  'id': 'aaaaaaaa-bbbb-1111-111qrazmataz',
  'product_id': 'BTC-USD',
  'side': 'buy',
  'stp': 'dc',
  'funds': '9.95024875',
  'specified_funds': '10',
  'type': 'market',
  'post_only': False,
  'created_at': '2020-07-18T16:45:03.722006Z',
  'fill_fees': '0',
  'btc_quantity': '0',
  'executed_value': '0',
  'status': 'pending',
  'settled': False
}
```

### GET ORDER (post purchase)
```
{
  'id': 'aaaaaaaa-bbbb-1111-111qrazmataz',
  'product_id': 'BTC-USD',
  'profile_id': '3333333333333333333333333333',
  'side': 'buy',
  'funds': '9.9502487500000000',
  'specified_funds': '10.0000000000000000',
  'type': 'market',
  'post_only': False,
  'created_at': '2020-07-06T00:21:00.390029Z',
  'done_at': '2020-07-06T00:21:00.394Z',
  'done_reason': 'filled',
  'fill_fees': '0.0497509230870000',
  'filled_size': '0.00109674',
  'executed_value': '9.9501846174000000',
  'status': 'done',
  'settled': True
}
```

### MARKET SALE RESPONSE
```
{'id': '74082a89-4206-4ba5-8d88-513157222dd9',
'size': '0.001',
'product_id': 'BTC-USD',
'side': 'sell',
'stp': 'dc',
'type': 'market',
'post_only': False,
'created_at': '2021-02-01T00:30:30.289238Z',
'fill_fees': '0',
'filled_size': '0',
'executed_value': '0',
'status': 'pending',
'settled': False}
```

### GET ORDER (post sale)
```
{
  'id': 'aaaaaaaa-bbbb-1111-111q-f00bar111',
  'size': '0.00063560',
  'product_id': 'BTC-USD',
  'profile_id': '060c2162-a79f-4708-b504-01fbf80b716b',
  'side': 'sell',
  'funds': '5.0000000000000000',
  'specified_funds': '5.0000000000000000',
  'type': 'market',
  'post_only': False,
  'created_at': '2021-01-30T19:04:43.481821Z',
  'done_at': '2021-01-30T19:04:43.489Z',
  'done_reason': 'filled',
  'fill_fees': '0.0249994058000000',
  'filled_size': '0.00014554',
  'executed_value': '4.9998811600000000',
  'status': 'done',
  'settled': True
}
