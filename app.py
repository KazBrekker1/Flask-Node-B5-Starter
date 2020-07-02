from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return render_template('main.html') #When you want to use templating
    return send_file('templates/index.html')
