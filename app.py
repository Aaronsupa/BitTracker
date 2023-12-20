from flask import Flask, request, render_template
import requests
from secret import KEY


app = Flask(__name__)
def fetch_data():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    headers = {
        "X-CoinAPI-Key": KEY 
    }
    response = requests.get(url, headers=headers)
    return response.json()


@app.route("/")
def bitApp():
    txt = fetch_data()
    time = txt['time']
    asset = txt['asset_id_base']
    assetQuote = txt['asset_id_quote']
    rate = txt['rate']
    data = [time, asset, assetQuote, rate]
    return render_template('index.html', data = data)

if __name__ == '__main__':
   app.run()
