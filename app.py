from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mathgame")
def mathgame():
    return render_template("mathgame.html")