from flask import Flask
app = Flask(__name__)

from flask import render_template
@app.route('/')
def home():
    return '這是首頁'

@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ =='__main__':
    app.run()