import sys, requests, pytest

def checkIP(location):
        try :
                r = requests.get(location)
                if "VulnApp" in str(r.content):
                        return("Good")
                else:
                        return("Error: Server not operational")
        except :
                return("Network error.  Server down.")
        
        

def main():
        #assume localhost
        ip = 'http://127.0.0.1'
        return checkIP(ip)

     

def test_server_online():
    assert main() == "Good"

