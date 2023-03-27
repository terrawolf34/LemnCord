import requests
import sys
sys.path.append("../..")
from token import token
tokenizor = token
guild_name = input("guild name? ")

# Define the headers to include the user token
headers = {
    "Authorization": f"{tokenizor}"
}

# Define the JSON payload to create the server
payload = {
    "name": f"{guild_name}"
}

# Send the POST request to create the server
response = requests.post("https://discord.com/api/v9/guilds", headers=headers, json=payload)

# Print the response
print(response.json())
