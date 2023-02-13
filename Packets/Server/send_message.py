import requests, sys; from Utils.Reader import *
sys.path.append("../..")

def send_message_server():
	Reader() #token

	channel_id = input("channel id?")
	url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
	auth = {
			'authorization': token} #token

	msg_content = input ("message?")

	msg = {
			'content':f"{msg_content}"
	}

	requests.post(url, headers = auth, data = msg)