import schedule
import time
import robin_stocks
import robin_stocks.robinhood as r
from secrets import USERNAME, PASSWORD, TAAPIKEY

# This is for logging into Robinhood using the robinstocks api

def login():
    r.login(USERNAME, PASSWORD)

login()
print("YOU ARE LOGGED IN TO ROBINHOOD")


# This is using the taapi API to find the current RSI of BTC on the 1 hr timeframe
def RSI():

  import requests

  indicator = "rsi"

  endpoint = f"https://api.taapi.io/{indicator}"

  parameters = {
    'secret': TAAPIKEY,
    'exchange': 'binance',
    'symbol': 'BTC/USDT',
    'interval': '1h'
  }

  response = requests.get(url=endpoint, params=parameters)

 # This is the output in JSON style
  result = response.json()
 # This is the RSI output as a float
  number = result["value"]

 # This is printing the current RSI value to the console
  print("The current RSI of BTC is: ")
  print(number)

  if number>=70:
    print("RSI ABOVE 70!! TIME TO SELL!!!!!!")
  elif number>30:
    print("RSI IN LIMBO RANGE")
  elif number<=30:
    print("RSI BELOW 30!! TIME TO BUY!!!!!")
  
  
  
  


  

# This is running "job" which is the function "RSI"
def job():
    RSI()

# This is running "hob" every 15 seconds to find the current RSI
schedule.every(.25).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


