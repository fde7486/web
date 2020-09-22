from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)

@app.route('/loop')
@app.route('/loop/<int:n>')
def loop(n=6):
    return render_template('loop.html',n=n)