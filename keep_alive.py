from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "I am alive and running!"

def run():
    # Render assigns a random port, but defaults to 10000. 
    # 0.0.0.0 makes it accessible to the outside world.
    app.run(host='0.0.0.0', port=7860)

def keep_alive():
    t = Thread(target=run)
    t.start()
