## TODO:
- pending sale problem
    when i sell, i'm not selling specific orders, rather the sum of their values.
    I need to figure out the best way to mark them pending and then track their
    final sale price after execution.


## example of coinbase get order response 
```
'id': '33f739ab-7908-4639-b972-3d662c7153ae',
'product_id': 'BTC-USD',
'profile_id': '060c2162-a79f-4708-b504-01fbf80b716b',
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
```
  

## example of coinbase purchase response 
```
'id': 'cc4820dk-fobar-28c5asack2373',
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
```

# Algorythm updates
- check for % of by vs sell
  - assuming this implies an iminent reversal of a trend
    - use this to inflate the buy amount
    - how can this make selling smarter?  I don't want to dump evertime there is a shift.

