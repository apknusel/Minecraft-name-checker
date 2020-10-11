import requests
import random
import string
import re
import time

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'api.mojang.com',
    'Origin': 'https://www.minecraft.com',
    'Referer': 'https://www.minecraft.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Siet': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

proxies = {}
usernames = []

def main():
    useprox = input("Use proxies? (Y/N): ")
    if useprox.upper() == "Y":
        get_proxies("proxies.txt")
    else:
        useless = 0
    useuser = input("Use usernames? (Y/N) ")
    if useuser.upper() == "N":
        number = input("How many letter usernames?: ")
        while True:
            username = get_random_string(number)
            if check(username) == True:
                print(username)
    else:
        i = 0
        get_usernames("usernames.txt")
        while i < len(usernames):
            username = usernames[i]
            if check(username) == True:
                print(username)
            i+=1
        print("Finished")

def get_usernames(usernamesfile):
    with open(usernamesfile, 'r') as f:
        for line in f:
            usernames.append(line.strip())

def get_proxies(filename):
    scheme = "http://"
    with open(filename, 'r') as f:
        for line in f:
            pr = line.strip()
            m = re.search(r'^(\d+\.\d+\.\d+\.\d+)\:(\d+)\:([^\:]*)\:([^\$]*)$', pr)
            if m:
                print('user: ' + m.group(3))
                proxies[scheme + m.group(1)] = scheme + m.group(3) + ':' + m.group(4) + '@' + m.group(1) + ':' + m.group(2)
            else:
                proxies[scheme + pr] = scheme + pr

def check(username):
    url = "https://api.mojang.com/user/profile/agent/minecraft/name/" + username
    req = requests.get(url, headers, proxies = proxies)
    if req.status_code == 200:
        return False
    if req.status_code == 200:
        return False
    if req.status_code == 429:
        time.sleep(45)
    else:
        return True

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

if __name__ == "__main__":
    main()
