from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return '<img src="https://i.postimg.cc/DwXTHVKb/b6834035-1f42-44bc-b013-090cfc91b9c4.jpg"></img>'
    # return render_template('index.html')


@app.route('/healthcheck')
def about():
    return 'OK', 200
