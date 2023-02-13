import requests, sys; from Utils.Reader import *
sys.path.append("../..")

def join_server():
    Reader() #token

    def join(server_invite):
        header = {"authorization": token}
        r = requests.post("https://discord.com/api/v8/invites/{}".format(server_invite), headers=header)

    join(token, input("invite? discord.gg/"))

#make sure your disc account has phone num else you risk locking it!