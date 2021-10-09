# Importing Flask Things
from flask import Flask, render_template

# Starting The App #
app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'


# Index
@app.route("/")
def index():
    return render_template("home.html")


# App Running
if __name__ == "__main__":
    app.run()