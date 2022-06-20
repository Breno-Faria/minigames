from flask import Flask, render_template, request, url_for, redirect
import psycopg2
import os
from boto.s3.connection import S3Connection

app = Flask(__name__, static_folder='static')

def connect_to_db():
    connection = psycopg2.connect(
        host=os.environ['host'],
        database=os.environ['database'],
        port=os.environ['port'],
        user=os.environ['user'],
        password=os.environ['password'],
    )
    return connection

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rules")
def rules():
    return render_template("rules.html")

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
        return redirect(url_for('mathleaderboard'))
    return render_template("mathgameover.html")

@app.route("/mathleaderboard")
def mathleaderboard():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM leaderboard ORDER BY score desc'
    )
    players = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("mathleaderboard.html", players=players)






@app.route("/gamemode2")
def gamemode2():
    return render_template("gamemode2.html")

@app.route("/gamemode2over", methods=('GET', 'POST'))
def gamemode2over():
    if request.method == 'POST':
        name = request.form['name']
        score = request.form['score']

        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO mode2leaderboard (name, score)'
            'VALUES (%s, %s)',
            (name, score)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('mode2leaderboard'))
    return render_template("gamemode2over.html")

@app.route("/mode2leaderboard")
def mode2leaderboard():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM mode2leaderboard ORDER BY score desc'
    )
    players = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("mode2leaderboard.html", players=players)