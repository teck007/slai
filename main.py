from flask import Flask
from flask import jsonify
from flask import request
from src.chat_openai import *

app = Flask(__name__)

@app.route('/shorten',methods=['POST'])
def hello():
    data = request.get_json()
    url = data['url']
    description = data['description']
    return jsonify({'shorten': shorten(url,description)})

if __name__ == '__main__':
    app.run(debug=True)