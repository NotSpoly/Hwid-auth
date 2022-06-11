import uuid
import requests
import subprocess
import os
import json
import time

def GetUUID():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\n") + 2
    uuid = uuid[pos1:-15]
    return uuid


print(GetUUID())

hwid2 = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
print(hwid2)
r = requests.get('pastbinlink')

hwid = GetUUID()

details = {
        "hwid": f"str{hwid}",
        "name": "Input",
}

with open("hwid.json", "w") as f:
    json.dump(details, f)

try:
    if hwid in r.text:
        pass
    else:
        print("[ERROR] HWID Not in database")
        print(f'Your HWID: {hwid}')
        time.sleep(5)
        os._exit()
except:
    print("[ERROR] Failed to connect to database")
    time.sleep(5)
    os._exit()

print("Authenticated")
