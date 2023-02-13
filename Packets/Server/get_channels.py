import requests, sys; from Utils.Reader import *
sys.path.append("../..")

def get_channels():
    Reader() #token

    headers = {
        "Authorization": token
    }

    def get_channels(guild_id):
        response = requests.get(f"https://discord.com/api/v6/guilds/{guild_id}/channels", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    guild_id = input("Enter the ID of the server you want to get channels for: ")
    channels = get_channels(guild_id)
    if channels:
        print(f"Channels for server with ID {guild_id}:")
        for channel in channels:
            print(f"Name: {channel['name']}, ID: {channel['id']}")
    else:
        print("Could not retrieve list of channels. Check your token and try again.")