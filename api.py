"""
Julius Caesar API
This API generates quotes from the very famous Roman emperor, Caesar.

Author: Ciro Goyeneche
"""

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()