import requests, sys; from colorama import Fore; from Utils.Reader import *
sys.path.append("../..")

def leave_server():
    Reader() #token

    endpoint = "https://discord.com/api/v6/users/@me/guilds/{guild_id}"


<<<<<<< HEAD
    endpoint = endpoint.format(guild_id=input("server id?"))

    headers = {
        "Authorization": "Bearer {}".format(token), #token
    }

    # Send a DELETE request to the API endpoint
    response = requests.delete(endpoint, headers=headers)

    # Check the response code to see if the request was successful
    if response.status_code == 204:
        print("Successfully left the server!")
    else:
        print(Fore.GREEN + '[DEBUG] Приколы всякие PARTY' + Fore.WHITE +  "Failed to leave the server. Response: {}".format(response.text))
=======
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
>>>>>>> bc2cc1bdd6ede145e5564283ebcb07cc79682239
