import requests
import json

DISCORD_USER_TOKEN = ""


MESSAGE_ID = input("message id? ")
CHANNEL_ID = input("channel id? ")

EMOJI_NAME = input("emoji in discord snowflake/with id? ") #need to be in discord snowflake

#%F0%9F%91%8D thumb up
#%F0%9F%98%84 happy grin

url = f"https://discordapp.com/api/v6/channels/{CHANNEL_ID}/messages/{MESSAGE_ID}/reactions/{EMOJI_NAME}/@me"


headers = {
    "Authorization": DISCORD_USER_TOKEN,
}

# Send the API request to add a reaction to the message
response = requests.put(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Reaction added successfully")
else:
    print(f"Failed to add reaction. Response: {response.text}")
