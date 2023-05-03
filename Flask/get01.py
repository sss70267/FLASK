from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '歡迎首頁(/get1)'

@app.route('/get1',methods = ['GET'])
def get():
    name = request.args.get('name')
    city = request.args.get('city')
    return render_template('get1.html',**locals())


if __name__ == '__main__':
    app.run()