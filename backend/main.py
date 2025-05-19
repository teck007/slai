from flask import Flask
from flask import jsonify
from flask import request
from src.chat_openai import shorten
from src.url_check import url_content
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/shorten',methods=['POST'])
def short():
    data = request.get_json()
    url = data['url']
    # description = data['description']
    content = url_content(url)
    return jsonify({'result': shorten(url,content)})

if __name__ == '__main__':
    app.run(debug=True)