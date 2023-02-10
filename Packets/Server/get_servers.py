import requests #https://discord.com/api/v9/users/@me/affinities/guilds
import sys
sys.path.append("../..")
from bruh import token
import os
# Replace <YOUR_TOKEN_HERE> with your actual Discord user token
headers = {
    "Authorization": token
}
def get_guilds():
    response = requests.get("https://discord.com/api/v6/users/@me/guilds", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

guilds = get_guilds()
if guilds:
    print("You are a member of the following servers:")
    for guild in guilds:
        print(f"Name: {guild['name']}, ID: {guild['id']}")
else:
    print("Could not retrieve list of servers. Check your token and try again.")