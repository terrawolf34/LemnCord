import requests
import sys
sys.path.append("../..")
from bruh import token

headers = {
    "Authorization": token
}

user_id = input("user id?")

response = requests.get(f"https://discord.com/api/v6/users/@me/channels", headers=headers)
if response.status_code != 200:
    print("Failed to retrieve list of direct message channels.")
    exit()

direct_message_channels = response.json()

# Find the direct message channel with the specified user
for dm in direct_message_channels:
    if dm["recipient"]["id"] == user_id:
        channel_id = dm["id"]
        break
else:
    print("Could not find a direct message channel with the specified user.")
    exit()

response = requests.get(f"https://discord.com/api/v6/channels/{channel_id}/messages", headers=headers)
if response.status_code != 200:
    print("Failed to retrieve messages in the direct message channel.")
    exit()

messages = response.json()
for message in messages:
    print(f"{message['author']['username']}#{message['author']['discriminator']}: {message['content']}")
