from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/echo_call/<param>') #get echo api
def get_echo_call(param):
    return jsonify({"param": param})

@app.route('/echo_call', methods=['POST']) #post echo api
def post_echo_call():
    param = request.get_json()
    return jsonify(param)

if __name__ == "__main__":
    app.run()