from flask import Flask, render_template, request
# import app
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/select/')
def select():
    return render_template("select.html")

@app.route('/play/')
def play():
    return render_template("play.html")

@app.route('/compute/')
def compute():
    return render_template("end.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
