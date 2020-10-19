import os
import subprocess
import sys
import json
import random
import requests
from datetime import datetime


# 추가해야 할것. api-key를 이용한 로그인 최초 1회만 설정해주면 됨.
# 문서에 json 형태로 저장할 것.
def login(api_key):
    if os.path.isdir(os.path.expanduser("~/Digo")) is False :
        os.mkdir(os.path.expanduser("~/Digo"))

    conn = requests.post("http://app.digo.ai:7777/digo-server/auto_digo/login", params={
        'api_key': api_key
    }).json()
    
    if conn['code'] is 0:
        info_json = {
            'api_key': api_key,
            'account_id': conn['account_id'],
            'session_key': conn['session_key'],
            'login_time': datetime.today().strftime("%Y/%m/%d %H:%M:%S")
        }
        
        file = open(os.path.expanduser("~/Digo/user_info.json"), mode="wt", encoding="utf-8")
        file.write(json.dumps(info_json, indent=4))
        file.flush()
        file.close()
        print("Welcom, Scucces Login ({0})".format(conn['account_id']))
    else:
        print("Login Fail, Not Valid API Key")


def auto_run(path, setting):

    if os.path.isdir(os.path.expanduser("~/Digo")) is False :
        print("Please login")
        return;

    file = open(os.path.expanduser("~/Digo/user_info.json"), mode="r", encoding="utf-8")
    login_data = json.loads(file.read())

    

    print("Welcom {0}, Run Code \"{1}\", Setting is \"{2}\"".format(login_data["account_id"], path, setting))

    fileDirectory = os.path.dirname(os.path.abspath(path))
    
    if os.path.exists(path) is False:
        raise Exception("Not Found File : Check Path {}".format(path))

    if os.path.exists(fileDirectory + os.path.sep + setting) is False:
        raise Exception("Not Found File : Check Setting File {}".format(fileDirectory + os.path.sep + setting))


    with open(fileDirectory + os.path.sep + setting) as ml_option_raw:
        ml_option = json.loads(ml_option_raw.read())


    adjectives = ['brilliant', 'adorable', 'shy', 'beautiful', 'popular', 'huge', 'curious', 'confident', 'assured', 'eager', 'energetic', 'loyal', 'nervous', 'careful', 'relaxed', 'calm', 'component', 'capable', 'talented', 'kind', 'wise', 'bright', 'busy', 'cool', 'cute', 'fair', 'fine', 'fresh', 'funny', 'grand', 'great', 'glad', 'humorous', 'lucky', 'nice', 'perfect', 'polite', 'proud', 'powerful', 'pretty', 'pure', 'quick', 'quiet', 'real', 'rich', 'right', 'royal', 'social', 'soft', 'safe', 'serious', 'simple', 'still', 'strong', 'thin', 'tiny', 'tired', 'virtual', 'weak', 'wide', 'warm', 'wild','young', 'lazy', 'lonely', 'large', 'angry', 'asleep', 'brave', 'active']

    auto_digo_name = random.choice(adjectives) + '-moly-' 
    numbers = "0123456789"
    for i in range(0, 4):
            auto_digo_name += random.choice(numbers)
# 
    conn = requests.post("http://app.digo.ai:7777/digo-server/auto_digo/createAutoDigo", params={
        'api_key': login_data['api_key'],
        'session_key': login_data['session_key'],
        'owner': login_data['account_id'],
        'run_path': path,
        'config': json.dumps(ml_option, indent=4),
        'name': auto_digo_name,
        'run_count' : ml_option['iterator']
    }).json()

    print(conn)

    file = open(os.path.expanduser("~/Digo/user_info.json"), mode="w", encoding="utf-8")
    login_data["auto_digo_name"] = conn["auto_digo_name"]
    login_data["auto_digo_id"] = conn["auto_digo_id"]
    file.write(json.dumps(login_data))
    file.flush()
    file.close()

    for i in range(ml_option["iterator"]):
        parameters = ['python', '-u', path, '-adname_fadg', auto_digo_name]


        for p in ml_option["parameter"]:
            
            if p["random"] == None or p["random"] == False :
                parameters.append(p["name"])
                if p["type"] != "None":
                    parameters.append(str(p["data"]))

            else :
                parameters.append(p["name"])
                if p["type"] == "float":
                    parameters.append(str(random.uniform(p["data"][0], p["data"][1])))
                elif p["type"] == "int":
                    parameters.append(str(random.randint(p["data"][0], p["data"][1])))
        
        print (parameters)
        proc = subprocess.Popen(parameters, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        message : str = "AUTODIGOSTART\n"
        proc.stdin.write(message.encode())
        proc.stdin.flush()

        while proc.poll() == None:
            nextLine = proc.stdout.readline().decode('utf-8')
            sys.stdout.write(nextLine)
            sys.stdout.flush()