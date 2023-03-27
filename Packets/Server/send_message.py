import requests
import sys
sys.path.append("../..")
from token import token

channel_id = input("channel id?")
url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
auth = {
		'authorization': token}
		
msg_content = input ("message?")
		
msg = {
		'content':f"{msg_content}"
}

requests.post(url, headers = auth, data = msg)


