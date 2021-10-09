from flask import Flask, render_template
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

api = requests.get("https://data.covidapi.com/countries").json()

# name = "Amirhossein"

@app.route("/")
def index():
    # return f"""
    #     <p>
    #         Country: <b>{api['body'][81]['country_name']}</b>
    #         |
    #         Total cases: <b>{api['body'][81]['total_cases']}</b>
    #         -
    #         Total deaths: <b>{api['body'][81]['total_deaths']}</b>
    #     </p>
    # """
    return render_template("index.html", len = len(api['body']), api = api['body'])