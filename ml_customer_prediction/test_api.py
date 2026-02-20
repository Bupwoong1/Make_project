from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'ML API is running'})

if __name__ == '__main__':
    print("Starting test server on http://localhost:8080")
    app.run(host='127.0.0.1', port=8080)
