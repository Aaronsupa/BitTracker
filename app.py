from flask import Flask, request, render_template
import requests
from secret import KEY
from datetime import datetime


app = Flask(__name__)
def fetch_data():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    headers = {
        "X-CoinAPI-Key": KEY 
    }
    response = requests.get(url, headers=headers)
    return response.json()


#'2023-12-20T17:18:36.0000000Z
@app.route("/")
def bitApp():
    txt = fetch_data()

    time = txt['time'].split("T") 
    date = time[0]
    time = time[1][:8]

    asset = txt['asset_id_base']
    assetQuote = txt['asset_id_quote']
    rate = txt['rate']
    data = [date, time, asset, assetQuote, rate]
    return render_template('index.html', data = data)

if __name__ == '__main__':
   app.run()
