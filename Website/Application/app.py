from flask import Flask, request

app = Flask(__name__, static_url_path='')

@app.route("/")
def root():
    pass

@app.route("/upload")
def upload():
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
    pass

@app.route("/endSession")
def endSession():
    pass

if __name__ == "__main__":
    app.run()