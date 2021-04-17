"""
Julius Caesar API
This API generates quotes from the very famous Roman emperor, Caesar.

Author: Ciro Goyeneche
"""
import random
import dotenv
from flask import Flask, request, jsonify

from utils import get_quotes_from_file

# Load .env config
dotenv.load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    info = {
        "message": 'Welcome to Caesar API',
        "actions": [
            'GET /quote'
        ]
    }
    return jsonify(info)

@app.route('/quote')
def quote():
    quotes = get_quotes_from_file('static/quotes.txt')
    quote = random.choice(quotes)
    response = {
        "quote": quote,
        "message": 'success'
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()