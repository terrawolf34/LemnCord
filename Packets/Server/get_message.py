import requests
import json

id = input("channel id?")
def retrieve_messages(channelid):
    num=0
    headers = {
        'authorization': ''
    }
    r = requests.get(
        f'https://discord.com/api/v9/channels/{channelid}/messages?limit=100',headers=headers #limit = amount of messages taken
        )
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(value['content'], '\n')
        num=num+1
    print('number of messages we collected is',num)

retrieve_messages(f'{id}')