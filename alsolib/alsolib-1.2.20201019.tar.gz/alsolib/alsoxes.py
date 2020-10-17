import urllib.request
class LoadWork:
    def __init__(self,pid):
        self.pid=pid
    def get_likes(self):
        try:
            url="http://code.xueersi.com/api/compilers/"+str(self.pid)+"?id="+str(self.pid)
            headers = {'Content-Type':'application/json'}
            a=requests.get(url=url, headers=headers)
            null,false,list_get,string=0,0,[],''
            p=json.loads(a.text)
            likes=p["data"]["likes"]
            return likes
        except:
            return -1
    def get_user(self):
        try:
            url = "http://code.xueersi.com/api/compilers/" + str(self.pid) + "?id=" + str(self.pid)
            print(url)
            headers = {'Content-Type': 'application/json'}
            a = requests.get(url=url, headers=headers)
            null, false, list_get, string = 0, 0, [], ''
            p = json.loads(a.text)
            return [p["data"]["username"], p["data"]["user_id"]]
        except:
            return -1
    def get_unlikes(self):
        try:
            url="http://code.xueersi.com/api/compilers/"+str(self.pid)+"?id="+str(self.pid)
            headers = {'Content-Type':'application/json'}
            a=requests.get(url=url, headers=headers)
            null,false,list_get,string=0,0,[],''
            p=json.loads(a.text)
            unlikes=p["data"]["unlikes"]
            return unlikes
        except:
            return -1
    def get_description(self):
        try:
            url='https://code.xueersi.com/api/compilers/v2/'+str(self.pid)+'?id='+str(self.pid)
            a=json.loads(urllib.request.urlopen(url).read().decode())
            return a['data']['description']
        except:
            return -1
    def get_codexml(self):
        try:
            url='https://code.xueersi.com/api/compilers/v2/'+str(self.pid)+'?id='+str(self.pid)
            a=json.loads(urllib.request.urlopen(url).read().decode())
            return a['data']['xml']
        except:
            return -1
    def get_name_as_pid(self):
        try:
            url='https://code.xueersi.com/api/compilers/v2/'+str(self.pid)+'?id='+str(self.pid)
            a=json.loads(urllib.request.urlopen(url).read().decode())
            return a['data']['name']
        except:
            return -1

    def is_like(self):
        url='http://code.xueersi.com/api/compilers/v2/'+str(self.pid)+'?id='+str(self.pid)
        data=json.loads(urllib.request.urlopen(url).read().decode())
        like1 = data['data']['likes']
        unlike1 = data['data']['unlikes']
        import time
        time.sleep(1)
        url='http://code.xueersi.com/api/compilers/v2/'+str(self.pid)+'?id='+str(self.pid)
        data=json.loads(urllib.request.urlopen(url).read().decode())
        like2 = data['data']['likes']
        unlike2 = data['data']['unlikes']
        if like2>like1:
            return 0
        elif unlike1>unlike2:
            return -1
        elif like1==like2 and unlike1==unlike2:
            return 1
def help():
    print(urllib.request.urlopen('http://www.asunc.cn/alsoxeshelp.txt').read().decode("gbk"))


import sys
def getCookies():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = ''
        except:
            pass
    return cookies

def jsonLoads(str):
    try:
        return json.loads(str)
    except:
        return None
import requests
import json


def get_fansnum(id):
    try:
        url = "http://code.xueersi.com/api/space/fans?user_id=" + str(id) + "&page=1&per_page=10"
        num = json.loads(requests.get(url).text)["data"]["total"]
        return num
    except:
        return -1