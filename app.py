from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    number_a = data.get('A', 0)
    number_b = data.get('B', 0)
    try:
        result = int(number_a) + int(number_b)
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide integers for A and B.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
