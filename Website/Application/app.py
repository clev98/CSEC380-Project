from flask import Flask, request, session, render_template, redirect, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from hashlib import sha256
from mysql import connector
from os import urandom
from logging import warning

#CHANGEME
StaticPath='/var/www/'
ID = str(urandom(64))

app = Flask(__name__, template_folder='templates')
app.secret_key = urandom(24)

#initialize database
db_connector = connector.connect(
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
limiter = Limiter(app, key_func=get_remote_address)
@limiter.limit("1440/day;60/hour;10/minute")
@app.route("/login", methods=['POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')

    # Get the salt
    query = "SELECT salt FROM User_Login WHERE Username=(%s);"
    cursor.execute(query, (username,))
    salt = cursor.fetchone()

    # hash
    hash = sha256((salt[0] + password).encode()).hexdigest()

    # Get hash from database
    query = "SELECT password_hash_salt FROM User_Login WHERE Username=(%s);"
    data = cursor.execute(query, (username,))
    result = cursor.fetchone()

    if(len(result) == 1):
        if(str(result[0]) == hash):
            session["ID"] = ID
            session["Username"] = username
            response = make_response(render_template('landing.html', name=session["Username"]))
            response.set_cookie("ID", ID)
            return response
        else:
            return render_template('index.html', error="Invalid Credentials")
    else:
        return render_template('index.html', error="Invalid Credentials")

#
@app.route("/landing", methods=['GET'])
def landing():
    if request.cookies.get("ID") == ID and "ID" in session:
        return render_template('landing.html', name=session["Username"])
    else:
        return render_template('index.html', error="Invalid Credentials")

#
@app.route("/delete/<file>", methods=['POST'])
def delete(file):
    if request.cookies.get("ID") == ID and "ID" in session:
        pass
    else:
        return render_template('landing.html', error="Don't delete other's videos!", name=session["Username"])

#
@app.route("/video/<file>", methods=['GET', 'POST'])
def video(file):
    if request.cookies.get("ID") == ID and "ID" in session:
        return render_template()

#
@app.route("/logout", methods=['GET'])
def logout():
    if request.cookies.get("ID") == ID and "ID" in session:
        session.pop("ID", None)
        session.pop("Username", None)
        return render_template('index.html', error="Logged Out")
    else:
        return render_template('index.html', error="Invalid Credentials")

#
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)