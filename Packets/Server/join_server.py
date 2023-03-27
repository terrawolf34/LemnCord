import requests
import sys
sys.path.append("../..")
from token import token

print('''If you don't have a phone number in your discord account
that is, there is a high chance that your account will be blocked and request your phone number!
Be careful with this! I warned you''')
 
def join(token, server_invite):
    header = {"authorization": token}
    r = requests.post("https://discord.com/api/v8/invites/{}".format(server_invite), headers=header)
    
join(token, input("invite? discord.gg/"))

#make sure your disc account has phone num else you risk locking it! (use quackr а почему бы и нет)
