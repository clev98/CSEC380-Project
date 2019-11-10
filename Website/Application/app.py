from flask import Flask, request
import mysql, hashlib
from mysql import connector

#CHANGEME
StaticPath='/var/www/'
StaticSalt = 'pL41qCFwnagJcZsM'

app = Flask(__name__, static_url_path='')

app.secret_key = os.urandom(24)
#initialize database
db_connector = mysql.conector.connect(
    host="db",
    user="root",
    password="absolutely_totally_secure",
    database="Application"
)

cursor = db_connector.cursor()

def get_file(filename):
    try:
        src = StaticPath + filename
        return open(src).read()
    except IOError as exc:
        return("No file file exists.  ya done fucked up.")

@app.route("/")
def root():
    content = get_file('index.html')
    return Response(content, mimetype='text/html')

@app.route("/login", methods=['POST'])
def login():
    username = request.get('user')
    password = request.get('password')
    hash = hashlib.sha3((StaticSalt + password).encode()).hexdigest()
    #get hash from database
    cursor.execute("SELECT password_hash_salt from User_Login WHERE Username like %s;", username)
    result = cursor.fetchone()
    if(str(result) == hash):
        #redirect
    pass
@app.route("/landing")
def landing():
    pass

@app.route("/delete/<file>")
def delete(file):
    pass

@app.route("/video/<file>")
def video(file):
    pass

@app.route("/logout")
def logout():
    pass

@app.route("/getSession")
def getSession():
    if "username" in session:
        return session
    return None

@app.route("/endSession")
def endSession():
    session.pop("username", None)
    
if __name__ == "__main__":
    app.run()