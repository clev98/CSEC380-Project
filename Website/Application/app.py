from flask import Flask, request, session, render_template, url_for, redirect, flash
import mysql, hashlib
from mysql import connector
import os
import time
import logging

#CHANGEME
StaticPath='/var/www/'

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

#initialize database
db_connector = mysql.connector.connect(
    host="db",
    user="armtube",
    password="absolutely_totally_secure",
    database="Application"
)

cursor = db_connector.cursor()

#
def get_file(filename):
    try:
        src = StaticPath + filename
        return open(src).read()
    except IOError as exc:
        return("No file file exists.")

@app.route("/", methods=['GET'])
def root():
    return render_template('index.html')

#
@app.route("/login", methods=['POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')

    # Get the salt
    query = "SELECT salt FROM User_Login WHERE Username=(%s);"
    cursor.execute(query, (username,))
    salt = cursor.fetchone()

    # hash
    hash = hashlib.sha256((salt[0] + password).encode()).hexdigest()

    # Get hash from database
    query = "SELECT password_hash_salt FROM User_Login WHERE Username=(%s);"
    data = cursor.execute(query, (username,))
    result = cursor.fetchone()

    if(len(result) == 1):
        logging.warning(username+":"+result[0]+","+hash)
        if(str(result[0]) == hash):
            session["username"] = username
            return redirect(url_for("landing"))
        else:
            return render_template('index.html', error="Invalid Credentials")
    else:
        return render_template('index.html', error="Invalid Credentials")

#
@app.route("/landing")
def landing():
    return render_template('landing.html')

#
@app.route("/delete/<file>")
def delete(file):
    pass

#
@app.route("/video/<file>")
def video(file):
    if "username" in session:
        return render_template()

#
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

#
@app.route("/getSession")
def getSession():
    if "username" in session:
        return session
    return None

#
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)