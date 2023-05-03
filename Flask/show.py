from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '這是首頁(show.html)'

@app.route('/show')
def show():
    person1 = {"name":"jojo","phone":"049-123456789","age":20}
    person2 = {"name":"naruto","phone":"0989777777","age":18}
    person3 = {"name":'sasuke',"phone":"0987888888","age":18}
    persons = [person1,person2,person3]

    return render_template('show.html',**locals())

if __name__ == '__main__':
    app.run()