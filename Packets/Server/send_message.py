import requests

channel_id = input("channel id?")
url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
auth = {
		'authorization': ""}
		
msg_content = input ("message?")
		
msg = {
		'content':f"{msg_content}"
}

requests.post(url, headers = auth, data = msg)


# name = input("Enter your name: ")
# print(f"Hello {name}")
# 773634174645043242
# 969616606869217342