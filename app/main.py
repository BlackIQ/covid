from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

@app.route("/")
def index():
    return render_template("index.html")