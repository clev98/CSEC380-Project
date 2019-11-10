import sys, requests, pytest

def checkValid():
    r = requests.post("http://localhost:5000/login", data={'username' : 'chaim', 'password': 'password'})
    if(r.url == "http://localhost:5000/landing"):
        return True
    else:
        return False
def checkInvalidPassword():
    r = requests.post("http://localhost:5000/login", data = {'username' : 'chaim', 'password': 'notapassword'})
    if(r.url == "http://localhost:5000/landing"):
        return False
    elif(r.url == "http://localhost:5000/login"):
        return True
    return False

def checkInvalidUser():
    r = requests.post("http://localhost:5000/login", data = {'username' : 'notchaim', 'password': 'password'})
    if(r.url == "http://localhost:5000/landing"):
        return False
    elif(r.url == "http://localhost:5000/login"):
        return True
    return False

def main():
    if(checkValid() and checkInvalidUser() and checkInvalidPassword()):
        return True
    else:
        return False

def test_server_online():
    assert main() == True