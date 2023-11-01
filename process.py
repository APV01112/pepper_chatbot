from flask import Flask, request, jsonify
import request_aws
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hi!'

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    user_input = data.get('question')
    return jsonify({"answer": request_aws(user_input).strip()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)