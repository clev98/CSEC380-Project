import sys, requests, pytest

def checkValid():
    s = requests.Session()
    r = s.post("https://localhost/login", verify=False, data={'username':'chaim', 'password':'password'})
    s.close()
    if(r.url == "https://localhost/landing"):
        return True
    else:
        return False
def checkInvalidPassword():
    s = requests.Session()
    r = s.post("https://localhost/login", verify=False, data = {'username':'chaim', 'password':'notapassword'})
    s.close()
    if(r.url == "https://localhost/landing"):
        return False
    elif(r.url == "https://localhost/login"):
        return True
    return False

def checkInvalidUser():
    s = requests.Session()
    r = s.post("https://localhost/login", verify=False, data = {'username':'notchaim', 'password':'password'})
    s.close()
    if(r.url == "https://localhost/landing"):
        return False
    elif(r.url == "https://localhost/login"):
        return True
    return False

def main():
    if(checkValid() and checkInvalidUser() and checkInvalidPassword()):
        return True
    else:
        return False

def test_server_online():
    assert main() == True
