from flask import Flask, request
import requests
import sympy

app = Flask(__name__)

TOKEN = "8018668374:AAFp5s0TiQzsEpw4cCxEjCycOAVjfosyVE4"
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def solve_math(expression):
    try:
        expr = sympy.sympify(expression)
        result = sympy.simplify(expr)
        return f"✅ Jawapan: {result}"
    except:
        return "❌ Maaf, saya tak faham soalan itu."

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        jawapan = solve_math(text)
        requests.post(TELEGRAM_API, json={"chat_id": chat_id, "text": jawapan})
    return "OK", 200
