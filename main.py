from websockets.sync.client import connect
import colorama
import os
import json
import requests
ids = []
total = 0
credits = 'By Failedtrades. On discord.'
def join(id, pet, value, host, game):
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
                requests.post('https://api.bloxybet.com/join_giveaway', headers=headers, json={'giveaway_id': id})
                if count == 0:
                    os.system('cls')
                    print(f'{colorama.Fore.GREEN}Joined giveaway')
                    print(
                        f"""{colorama.Fore.RESET}
Host {host}       Pet {pet}          Total joined today
Game {game}             Rap {value}                        {total}
"""
                    )
                count += 1
while True:
    print(f'{colorama.Fore.YELLOW}connecting to websocket! {credits}')
    try:
        headers = {
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
  "Cache-Control": "no-cache",
  "Connection": "Upgrade",
  "Host": "api.bloxybet.com",
  "Origin": "https://www.bloxybet.com",
  "Pragma": "no-cache",
  "Upgrade": "websocket",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

        with connect('wss://api.bloxybet.com/giveaway_ws', additional_headers=headers) as websocket:
            os.system('cls')
            print(f'{colorama.Fore.GREEN}connected to websocket! {credits}')
            while True:
                raw_msg = websocket.recv()
                
                # Check if the received message is a valid JSON string
                if 'heartbeat' in raw_msg:
                    
                    continue
                else:
                    msg = json.loads(raw_msg)
                    if msg['_id'] in ids:
                        pass       
                    else:
                        
                        print(f'Joining giveaway {credits}')
                        ids.append(msg["_id"])
                        total += msg['item']['value']
                        join(msg['_id'], msg['item']['display_name'], msg['item']['value'], msg['host']['username'], msg['item']['game'])
    except Exception as e:
        print(f'{colorama.Fore.RED} Error connecting. {credits}\nERROR: {e}\nask for support')
