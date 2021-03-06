import os

from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello World!"


if __name__ == "__main__":
  app.run(
    port=int(os.environ.get('FLASK_PORT', 5000)),
    host='0.0.0.0'
  )
