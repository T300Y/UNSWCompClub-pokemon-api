from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        "Hello!": "HEHEHEHHEHEHE"
    }
    return jsonify(data)

# fake