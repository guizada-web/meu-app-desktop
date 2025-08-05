from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/gato')
def gato():
    res = requests.get('https://api.thecatapi.com/v1/images/search')
    data = res.json()
    return jsonify({'url': data[0]['url']})

if __name__ == '__main__':
    app.run(debug=True)