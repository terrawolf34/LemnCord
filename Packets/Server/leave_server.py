import requests
import sys
sys.path.append("../..")
from bruh import token


headers = {
    "Authorization": token
}

def leave_server(guild_id):
    response = requests.delete(f"https://discord.com/api/v6/users/@me/guilds/{guild_id}", headers=headers)
    if response.status_code == 204:
        return True
    else:
        return False

guild_id = input("Enter the ID of the server you want to leave: ")
if leave_server(guild_id):
    print("Left server successfully!")
else:
    print("Could not leave server. Check your token and try again.")
