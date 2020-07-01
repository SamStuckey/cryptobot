```
robinhood_username  = 'sam.n.stuckey@gmail.com' 
robinhood_password  = 'J$1wb@m10y8923'
rh_client = Robinhood()
rh_client.login(username=robinhood_username, password=robinhood_password)
rh_client.place_market_buy_order(symbol='BTC', time_in_force='GFD', quantity=0.01)
```
Example POST to http://nummus.robinhood.com/orders to buy BTC
```
request 1:

account_id: "RH_ACC_NUMMUS_HASH"
average_price: null
cancel_url: "https://nummus.robinhood.com/orders/6876b84c-e9af-408c-8bf1-ed81f1cc9a82/cancel/"
created_at: "2020-07-01T11:15:25.414828-04:00"
cumulative_quantity: "0.000000000000000000"
currency_pair_id: "3d961844-d360-45fc-989b-f6fca761d511"
executions: []
id: "6876b84c-e9af-408c-8bf1-ed81f1cc9a82"
last_transaction_at: null
price: "9344.190000000000000000"
quantity: "0.001080880000000000"
ref_id: "7b4158d7-ffc9-48a0-a764-663b464bff55"
rounded_executed_notional: "0.00"
side: "buy"
state: "unconfirmed"
time_in_force: "gtc"
type: "market"
updated_at: "2020-07-01T11:15:25.557341-04:00"

request 2:

account_id: "RH_ACC_NUMMUS_HASH"
average_price: null
cancel_url: "https://nummus.robinhood.com/orders/8db30e31-b810-41a3-8edf-09769a852342/cancel/"
created_at: "2020-07-01T11:42:02.192474-04:00"
cumulative_quantity: "0.000000000000000000"
currency_pair_id: "3d961844-d360-45fc-989b-f6fca761d511"
executions: []
id: "8db30e31-b810-41a3-8edf-09769a852342"
last_transaction_at: null
price: "9353.870000000000000000"
quantity: "0.001619650000000000"
ref_id: "236e30cc-507d-4ef5-b22a-8cb4506550d1"
rounded_executed_notional: "0.00"
side: "buy"
state: "unconfirmed"
time_in_force: "gtc"
type: "market"
updated_at: "2020-07-01T11:42:02.326946-04:00"
```

# Cryptobot-V1


## TODO:
1. place order
  - successfully trigger market buy
  - record transaction to database with applicable feilds

2. load profitable orders
  - write SQLAlchamey query to load orders as commented

3. Sell orders
  - execute a market sale
