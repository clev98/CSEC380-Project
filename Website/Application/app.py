from flask import Flask, request, session, render_template, url_for, redirect
import mysql, hashlib
from mysql import connector
import os

#CHANGEME
StaticPath='/var/www/'

app = Flask(__name__, static_url_path='')
app.secret_key = os.urandom(24)

#initialize database
db_connector = mysql.connector.connect(
    host="db",
    user="root",
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
    username = request.get('user')
    password = request.get('password')

    # Get the salt
    cursor.execute("SELECT salt FROM User_Login WHERE Username LIKE %s;", username)
    salt = cursor.fetchone()

    # hash
    hash = hashlib.sha3((StaticSalt + password).encode()).hexdigest()

    # Get hash from database
    query = "SELECT password_hash_salt from User_Login WHERE Username LIKE (%s);"
    data = cursor.execute(query, (user,))
    result = cursor.fetchall()
    if(len(result) == 1):
        if(str(result[0][0]) == hash):
            session["username"] = username
            return redirect(url_for("landing"))
    else:
        error = "Invalid Credentials"
        return render_template('index.html', error=error)

#
@app.route("/landing")
def landing():
    pass

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
    app.run()