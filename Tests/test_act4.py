import sys, requests, pytest, json

#nested elses are disgusting.
def checkValid():
    s = requests.Session()
    r = s.post("https://localhost/login", verify=False, data={'username':'test', 'password':'password'})
    if(r.url == "https://localhost/landing" == False):
        print("failure at 1")
        return False
    r = s.post("https://localhost/upload_link",verify=False, data={"linkfile":"https://csec380.sp1kedshell.ninja/important_notes.mp4"})
    r = s.get("https://localhost/static/videos/important_notes.mp4", verify=False)
    if(r.status_code != 200):
        print("failure at 2")
        return False
    r = s.get("https://localhost/get_id/important_notes.mp4")
    id = json.loads(r.content.decode())['id']
    r = s.get("https://localhost/delete/" + str(id))
    print(str(id))
    print(r.url)
    print(r.content)
    r = s.get("https://localhost/get_id/important_notes.mp4")
    id = int(json.loads(r.content.decode())['id'])
    print(id)
    if(id != -1):
        print("failure at 3")
        return False
    s.close()
    return True
        

def main():
    if(checkValid()):
        return True
    else:
        return False

def test_server_online():
    assert main() == True
