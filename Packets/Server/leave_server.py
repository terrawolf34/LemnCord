import requests, sys; from colorama import Fore; from Utils.Reader import *
sys.path.append("../..")

def leave_server():
    Reader() #token
    
    endpoint = "https://discord.com/api/v6/users/@me/guilds/{guild_id}"
    
    
    endpoint = endpoint.format(guild_id=input("server id?"))
    
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