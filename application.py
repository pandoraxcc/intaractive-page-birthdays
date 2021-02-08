import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
import psycopg2
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")
results = db.execute("SELECT id, name, month, day FROM birthdays")


@app.route("/", methods=["GET", "POST"])
def index():
    # TODO: Display the entries in the database on index.html
    if request.method == "POST":
        name = request.form['name']
        month = request.form['month']
        day = request.form['day']
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (? ,? ,? )", name, month, day)
        return redirect("/")
    else:
        results = db.execute("SELECT id, name, month, day FROM birthdays")
        return render_template("index.html", output_data=results)
