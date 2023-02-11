import requests
import json
import sys
sys.path.append("../..")
from bruh import token


headers = {
    "Authorization": token
}

def get_user(user_id):
    response = requests.get(f"https://discord.com/api/v6/users/{user_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_channel_messages(channel_id):
    response = requests.get(f"https://discord.com/api/v6/channels/{channel_id}/messages", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
channel_id = input("What Channel should we get the messages from? ")
messages = get_channel_messages(channel_id)
if messages:
    print("Messages in this channel:")
    for message in reversed(messages):
        user = get_user(message["author"]["id"])
        if user:
            print(f"Username: {user['username']}#{user['discriminator']}, Message: {message['content']}")
        else:
            print(f"Username: (could not retrieve), Message: {message['content']}")
else:
    print("Could not retrieve messages. Check your token and try again.")
