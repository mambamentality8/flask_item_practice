from manage import app
from . import index_blu

@app.route("/")
def hello_world():
    return "hello world!"

@index_blu.route('/index')
def index():
    return 'index'