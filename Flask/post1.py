from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return 'post網頁練習'

@app.route('/post1')
def post1():
    return render_template('post.html')

@app.route('/submit',methods = ['POST'])
def submit():
    username = request.values['username']
    password = request.values['password']

    if username == '鄭詠升' and password == '55688':
        return '練習網站'

    else:
        return '帳號錯誤'

if __name__ == '__main__':
    app.run()