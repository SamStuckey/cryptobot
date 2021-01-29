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

