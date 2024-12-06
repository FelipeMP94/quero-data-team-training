from key import API_KEY
import requests 

url = "https://api.stockdata.org/v1/data/eod"

 
params = {
    "api_token": API_KEY,
    "symbols": ["AAPL","AMZN"]
}

def main():

    response = requests.get( url,params=params)
    print(response.text)

if __name__ == "__main__":
    main()