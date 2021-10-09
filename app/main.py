from flask import Flask, render_template
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

api = requests.get("https://data.covidapi.com/countries").json()

name = "Amirhossein"

# for i in range(195):
#     return f"<p>{api['body'][i]['country_name']}</p>"

@app.route("/")
def index():
    # return render_template("index.html")
    return f"Welcome to covid api <b>{name}</b>"