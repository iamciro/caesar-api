"""
Julius Caesar API
This API generates quotes from the very famous Roman emperor, Caesar.

Author: Ciro Goyeneche
"""
import dotenv

from flask import Flask

# Load .env config
dotenv.load_dotenv()

app = Flask(__name__)

if __name__ == "__main__":
    app.run()