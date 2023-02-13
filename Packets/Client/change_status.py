import requests, json, sys; from Utils.Reader import *
sys.path.append("../..")

def change_status():
    Reader() #token

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    def change_about(about):
        data = {"description": about}
        response = requests.patch("https://discord.com/api/v6/users/@me", headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return True
        else:
            return False

    about = input("Enter your desired about text: ")
    if change_about(about):
        print("About text changed successfully!")
    else:
        print("Could not change about text. Check your token and try again.")