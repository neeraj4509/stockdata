from flask import Flask, jsonify, request
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/stock', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol', default="", type=str)
    stock = yf.Ticker(symbol)

    # Fetching the required data
    todays_data = stock.history(period="1d")
    info = stock.info

    stock_details = {
        "live_price": todays_data['Close'].iloc[-1] if not todays_data.empty else "N/A",
        "today_high": todays_data['High'].iloc[-1] if not todays_data.empty else "N/A",
        "today_low": todays_data['Low'].iloc[-1] if not todays_data.empty else "N/A",
        "open_price": todays_data['Open'].iloc[-1] if not todays_data.empty else "N/A",
        "dividend": info.get('dividendYield', "N/A")
    }

    return jsonify(stock_details)

if __name__ == '__main__':
    app.run(debug=True)
