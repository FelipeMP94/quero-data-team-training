import os
from dotenv import load_dotenv
import requests 
import json

url = "https://api.stockdata.org/v1/data/eod"
load_dotenv()
API_KEY = os.getenv("API_KEY")

stocks = ["AAPL","AMZN","UNH","TSLA","NVDA","GOOG"," META","INTR","TSM","NFLX "]

start_date =  "2024-11-03"
end_date = "2024-11-16"

all_stocks = []
def main():
    for stock in stocks:
        params = {"api_token": API_KEY,"symbols": stock,"date_from":start_date,"date_to":end_date }
        response = requests.get( url,params=params)
        data = response.json()
        all_stocks.append(data)
    print(all_stocks)
    print(type(all_stocks))
    with open('bronze/stocks_bronze.json', "w", encoding="utf-8") as arquivo:
        json.dump(all_stocks, arquivo, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()