from datetime import datetime

from flask import Flask
app = Flask(__name__)

from flask import render_template
@app.route('/')
def home():
    return '這是首頁099'

@app.route('/hello1')
def hello1():
    return render_template('hello.html')

#@app.route('/hello2/<string:name>')
#def hello2(name):
#    now = datetime.now()
#    return render_template('hello2.html',**locals())

@app.route('/hello3/<string:name>')
def hello2(name):
    now = datetime.now()
    return render_template('hello3.html',**locals())

if __name__ =='__main__':
    app.run()