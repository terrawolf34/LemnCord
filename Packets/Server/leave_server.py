import requests

# Define the user token
token = ""

# Define the Discord API endpoint for leaving a server
endpoint = "https://discord.com/api/v6/users/@me/guilds/{guild_id}"

# Replace `{guild_id}` with the ID of the server you want to leave
endpoint = endpoint.format(guild_id=input("server id?"))

# Set the headers for the API request
headers = {
    "Authorization": "Bearer {}".format(token),
}

# Send a DELETE request to the API endpoint
response = requests.delete(endpoint, headers=headers)

# Check the response code to see if the request was successful
if response.status_code == 204:
    print("Successfully left the server!")
else:
    print("Failed to leave the server. Response: {}".format(response.text))
