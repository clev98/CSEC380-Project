import sys, requests, pytest

#eh, mildly disgusting, but it does work.  In the future use some kind of unique identifier to figure out if it's correct.
teststr = 'b\'<!DOCTYPE html>\\n<html lang="en">\\n<head>\\n\\t<title>Project: Hello World</title>\\n</head>\\n<body>\\n\\t<h1>CSEC380: VulnApp</h1>\\n\\t<p>Hello World</p>\\n</body>\\n</html>\\n\''

def checkIP(location):
        try :
                r = requests.get(location)
                if(str(r.content) == teststr):
                        return("Good")
                else:
                        return("Error: Server not operational")
        except :
                return("Network error.  Server down.")
        
        

def main():
        #assume localhost
        ip = 'http://127.0.0.1:80'
        return checkIP(ip)

     

def test_server_online():
    assert main() == "Good"

