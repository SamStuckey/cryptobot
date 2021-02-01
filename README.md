# WIPN TESt
## TODO:
- update trend reversal logic to use velocity or buy / sell ratio
    I can make this way smarter by watching for shifts in market trends
    instead of hard numbers.  I think this will work best for buying, as it
    can indicate the approach of a floor.  
    However, it's a little fuzzier on sales, as we want to avoid false positives.
    Maybe set up a more refined sale trigger that watches for both percentange
    changes and downticks, in conjunction with a hard stop loss below peaks.
- balance not found problem
    right now, my client is just returning 0 instead of None, but wtf...
    why is my balance not always found?  what are the potential implications of 
    this?
    - race condition?
- gummy sale mechanics...
    selling all orders works via a simple test run, but when in the context of the
    websocket it fails.

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
