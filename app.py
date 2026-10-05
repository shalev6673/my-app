import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from OpenShift Python S2I (Unencrypted HTTP)!</h1>"

@app.route('/health')
def health():
    return jsonify(status="UP"), 200

if __name__ == '__main__':
    # Default to port 8080 as expected by OpenShift
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
