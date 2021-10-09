from flask import Flask, render_template
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

api = requests.get("https://data.covidapi.com/countries")
api = api.json()

@app.route("/")
def index():
    # return render_template("index.html")
    return "Welcome to covid api"