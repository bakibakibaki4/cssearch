from flask import Flask, jsonify, request
from flask_cors import CORS
import httpx

app = Flask(__name__)
CORS(app, origins=[
    "https://cssearch-lac.vercel.app",
    "http://localhost:5000",
    "null"
])

@app.route("/")
def health():
    return jsonify({"status": "ok"})

@app.route("/items")
def items():
    try:
        with httpx.Client() as client:
            r = client.get(
                "https://api.skinport.com/v1/items",
                params={"app_id": 730, "currency": "EUR", "tradable": 0},
                timeout=15
            )
            return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/prices/waxpeer")
def waxpeer():
    skin = request.args.get("skin", "")
    try:
        with httpx.Client() as client:
            r = client.get(
                "https://api.waxpeer.com/v1/get-items-list",
                params={"game": "csgo", "search": skin, "sort": "ASC", "order": "price", "limit": 5},
                timeout=10
            )
            return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/prices/dmarket")
def dmarket():
    skin = request.args.get("skin", "")
    try:
        with httpx.Client() as client:
            r = client.get(
                "https://api.dmarket.com/exchange/v1/market/items",
                params={"gameId": "a8db", "title": skin, "currency": "EUR", "limit": 1, "orderBy": "price", "orderDir": "asc"},
                timeout=10
            )
            return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
