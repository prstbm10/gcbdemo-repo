from flask import Flask
import os
import sockett

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello Everyone!</h3>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
