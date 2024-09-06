API_KEY="5f80604f235a47836d5f5de3b02f83a1-e1fb1333da9e90f26233430924d08204" # TODO Change for different ACCOUNTS
API_URL="https://api-fxpractice.oanda.com/v3"
ACCOUNT_ID="101-001-29791862-001" # TODO Change for different ACCOUNTS
MONGO_CONN_STR="mongodb+srv://admin:admin@cluster0.0k8hzmo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

SECURE_HEADER={
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type" : "application/json"
}
BUY=1
SELL=-1
NONE=0

INVESTING_COM_PAIRS = {
   "EUR_USD":{
      "pair":"EUR_USD",
      "pair_id":1
   },
   "GBP_USD":{
      "pair":"GBP_USD",
      "pair_id":2
   },
   "USD_JPY":{
      "pair":"USD_JPY",
      "pair_id":3
   },
   "USD_CHF":{
      "pair":"USD_CHF",
      "pair_id":4
   },
   "AUD_USD":{
      "pair":"AUD_USD",
      "pair_id":5
   },
   "EUR_GBP":{
      "pair":"EUR_GBP",
      "pair_id":6
   },
   "USD_CAD":{
      "pair":"USD_CAD",
      "pair_id":7
   },
   "NZD_USD":{
      "pair":"NZD_USD",
      "pair_id":8
   },
   "EUR_JPY":{
      "pair":"EUR_JPY",
      "pair_id":9
   },
   "EUR_CHF":{
      "pair":"EUR_CHF",
      "pair_id":10
   },
   "GBP_JPY":{
      "pair":"GBP_JPY",
      "pair_id":11
   },
   "GBP_CHF":{
      "pair":"GBP_CHF",
      "pair_id":12
   },


   "EUR_CAD":{
      "pair":"EUR_CAD",
      "pair_id":16
   },










}

TFS = {
   "M5": 300,
   "M15": 900,
   "H1": 3600,
   "D": 86400
}