import requests
import sys
sys.path.append("../..")
from bruh import token

 
def join(token, server_invite):
    header = {"authorization": token}
    r = requests.post("https://discord.com/api/v8/invites/{}".format(server_invite), headers=header)
    
join(token, input("invite? discord.gg/"))

#make sure your disc account has phone num else you risk locking it! (use quackr а почему бы и нет)
