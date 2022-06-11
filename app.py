from flask import Flask, render_template, request, url_for, redirect
import psycopg2
import os

app = Flask(__name__)

def connect_to_db():
    connection = psycopg2.connect(
        host="localhost",
        database="games_project",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
    )
    return connection

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mathgame")
def mathgame():
    return render_template("mathgame.html")

@app.route("/mathgameover", methods=('GET', 'POST'))
def mathgameover():
    if request.method == 'POST':
        name = request.form['name']
        score = request.form['score']

        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO leaderboard (name, score)'
            'VALUES (%s, %s)',
            (name, score)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('home'))
    return render_template("mathgameover.html")