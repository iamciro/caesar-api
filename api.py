"""
Julius Caesar API
This API generates quotes from the very famous Roman emperor, Caesar.

Author: Ciro Goyeneche
"""
import dotenv

dotenv.load_dotenv()

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()