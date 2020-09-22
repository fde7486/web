from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/hello', defaults={'name': 'Someone'})
@app.route("/hello/<name>")
@app.route("/hi/<name>")
def hello(name):
    return 'Hello, {}!'.format(name)


@app.route('/<int:str>')
def get_int(str):
    return "INT : {}".format(str)
    
@app.route('/<float:str>')
def get_float(str):
    return "Float : {}".format(str)

@app.route('/<string:str>')
def get_string(str):
    return "STR : {}".format(str)

@app.route('/<path:str>')
def get_path(str):
    return "Path : {}".format(str)