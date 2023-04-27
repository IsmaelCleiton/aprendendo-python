from flask import Flask,render_template
from markupsafe import escape

app = Flask('Training')

@app.route('/')
def helloworld():
    return "<p>Hello World</p>"

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html',name = name)

@app.route('/projects/')
def projects():
    return  projects
app.run()