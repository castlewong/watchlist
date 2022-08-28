


from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return '<h1>Welcome to My Watchlist!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="https://tva1.sinaimg.cn/large/008i3skNly1gxdozl40zmj30ry0ut0wn.jpg">'

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    return 'Test page'


