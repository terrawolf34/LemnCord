import json
import time
import websocket
import requests
import os
import sys
sys.path.append("../..")
from token import token


status = "online"



headers = {"Authorization": os.getenv("TOKEN"), "Content-Type": "application/json"}
userinfo = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
username = "this"
discriminator = "is"
userid = "broken"

def onliner(token, status):
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    auth = {"op": 2,"d": {"token": token,"properties": {"$os": "Windows 10","$browser": "Google Chrome","$device": "Windows"},"presence": {"status": status,"afk": False}},"s": None,"t": None}
    ws.send(json.dumps(auth))
    online = {"op":1,"d":"None"}
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps(online))

def run_onliner():
  os.system("clear")
  print(f"Logged in as {username}#{discriminator} ({userid}).")
  while True:
    onliner(os.getenv("TOKEN"), status)
    time.sleep(30)

run_onliner()
