from manage import app
from . import index_blu

@index_blu.route("/")
def hello_world():
    return "hello world!"

@index_blu.route('/index')
def index():
    return 'index'