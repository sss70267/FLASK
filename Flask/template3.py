from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def home():
    return '這是首頁'

@app.route('/variable')
def variable():
    student = {'學號:':'70267','姓名':'鄭詠升','性別':'男'}
    fruit = ['蘋果','香蕉','芭樂','百香果']
    return  render_template('variable.html',**locals())

if __name__ =='__main__':
    app.run()