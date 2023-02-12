import requests, sys; from Utils.Reader import *
sys.path.append("../..")

def dm_message():
    Reader() #token

    def sendMessage(channel_id, message):
        url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
        data = {"content": message}
        header = {"authorization": token}
    
        r = requests.post(url, data=data, headers=header)
        print(r.status_code)
    
    
    def createDmChannel(user_id):
        data = {"recipient_id": user_id}
        headers = {"authorization": token}
    
        r = requests.post(f'https://discord.com/api/v9/users/@me/channels', json=data, headers=headers)
        print(r.status_code)
    
        channel_id = r.json()['id']
    
        return channel_id
    
    
    #Change these variables
    user_id = input("userid? ")
    message = input("message? ")
    
    channel_id = createDmChannel(token, user_id)
    sendMessage(token, channel_id, message)


    #CURRENTLY NOT WORK DISCORD FUCKED IT UP.....
    #it worked 2 days ago :(