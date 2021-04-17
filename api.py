"""
Julius Caesar API
This API generates quotes from the very famous Roman emperor, Caesar.

Author: Ciro Goyeneche
"""
import dotenv
from flask import Flask, jsonify

# Load .env config
dotenv.load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    info = {
        "message": "Welcome to Caesar API",
        "actions": [
            "GET /quote"
        ]
    }
    return jsonify(info)

if __name__ == "__main__":
    app.run()