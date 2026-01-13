from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RAPIDAPI_KEY = "PASTE_YOUR_RAPIDAPI_KEY"
RAPIDAPI_HOST = "indian-railway-irctc.p.rapidapi.com"

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()

    reply = "🚆 Train search received.\n"
    reply += "👉 Book here: https://www.confirmtkt.com/?affid=YOURID"

    return jsonify({"fulfillmentText": reply})

if __name__ == "__main__":
    app.run()
