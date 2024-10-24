import os
import threading
from time import time
from flask import Flask

@app.route('/')
def hello_world():
    return 'Hello, World!'    

def run_flask():
    app.run(host="0.0.0.0", port=5234)

if __name__ == "__main__":
    app = Flask(__name__)
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()