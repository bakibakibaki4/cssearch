from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, origins=[
    "https://cssearch-lac.vercel.app",
    "http://localhost:5000",
    "null"
])

HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "br, gzip, deflate"
}

@app.route("/")
def health():
    return jsonify({"status": "ok"})

@app.route("/items")
def items():
    try:
        r = requests.get(
            "https://api.skinport.com/v1/items",
            params={"app_id": 730, "currency": "EUR", "tradable": 0},
            headers=HEADERS, timeout=15
        )
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/prices/waxpeer")
def waxpeer():
    skin = request.args.get("skin", "")
    try:
        r = requests.get(
            "https://api.waxpeer.com/v1/prices",
            params={"game": "csgo", "search": skin},
            headers=HEADERS, timeout=10
        )
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/prices/dmarket")
def dmarket():
    skin = request.args.get("skin", "")
    try:
        r = requests.get(
            "https://api.dmarket.com/exchange/v1/market/items",
            params={"gameId": "a8db", "title": skin, "currency": "EUR", "limit": 1},
            headers=HEADERS, timeout=10
        )
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
