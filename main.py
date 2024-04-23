import requests, json, time, os

api = "https://api.bloxybet.com/giveaways/active"
headers = {
    "Accept": "*/*",
    "Origin": "https://www.bloxybet.com",
    "Priority": "u=1, i",
    "Referer": "https://www.bloxybet.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
ids = []
total = 0
credits = 'By Failedtrades. On discord.'
recent = {
    "id": None,
    "game": None,
    "host": None,
    "value": None,
    "pet": None,
}
def join(id):
    count = 0
    auths = json.load(open('settings.json'))['auths']
    for i in range(0,3):
        for x in auths:
            if credits == 'By Failedtrades. On discord.':
                headers = {
                    "authority": "api.bloxybet.com",
                    "method": "GET",
                    "path": "/profile",
                    "scheme": "https",
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                    "Authorization": f"{x}",
                    "Origin": "https://www.bloxybet.com",
                    "Referer": "https://www.bloxybet.com/",
                    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": "\"Windows\"",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
                res = requests.post('https://api.bloxybet.com/join_giveaway', headers=headers, json={'giveaway_id': id})
                if count == 0:
                    print(f'joined Giveaway Stated above\n\nAPI RESPONSE > {res.json()['message']}')
                count += 1
while True:
    os.system('cls')
    print('Refreshing V2 API')
    v2 = requests.get(api, headers=headers)
    os.system('cls')
    if v2.status_code == 200:
        try:
            response = v2.json()
            for i in response['giveaways']:
                if i['_id'] not in ids:
                    ids.append(i['_id'])
                    total += i['item']['value']
                    print(
                        f"""
MOST RECENT GIVEAWAY                                                     Total Value joined today
Host {i['host']['username']}       Pet {i['item']['display_name']}                                {total}
Game {i['item']['game']}                Value {i['item']['value']}                

GIVEAWAY API RESPONSE > {v2.json()['message']}
"""
                    )
                    recent['game'] = i['item']['game']
                    recent["host"] = i['host']['username']
                    recent["id"] = i['_id']
                    recent["pet"] = i['item']['display_name']
                    recent["value"] = i['item']['value']
                    join(i['_id'])
                else:
                    print(
                        f"""
MOST RECENT GIVEAWAY                                                     Total Value joined today
Host {i['host']['username']}       Pet {i['item']['display_name']}                                {total}
Game {i['item']['game']}                Value {i['item']['value']}      

WAITING FOR NEW GIVEAWAYS
"""
                    )
            
        except Exception as error:
            print(f'[ERROR] Contact support or a dev\n\n[DEV INFO]\nAPI Status code {v2.status_code}\nException {error}')
            break
    else:
        print(f'[ERROR] Contact support or a dev\n\n[DEV INFO]\nAPI Status code {v2.status_code}\nAPI error {v2.text}')
        break
    time.sleep(5)

