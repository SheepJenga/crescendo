from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes


@app.route("/", methods=["GET"])
def index():
    return {'score': 1}

@app.route("/testing")
def test():
    return {'testing': 123}

if __name__ == "__main__":
    app.run(port=8080)