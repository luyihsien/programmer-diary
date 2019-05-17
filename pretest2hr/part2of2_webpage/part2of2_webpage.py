#啟動直譯自己去自己的本地端網頁就能看到網頁
# http://127.0.0.1:5000/
from flask import Flask
import requests
res = requests.get('http://wiki.python.org.tw/The%20Zen%20Of%20Python')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return res.text


if __name__ == '__main__':
    app.run()
