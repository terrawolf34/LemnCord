import os

print("""╭╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╭╮
┃┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱┃┃
┃┃╱╱╭━━┳╮╭┳━╮┃┃╱╰╋━━┳━┳━╯┃
┃┃╱╭┫┃━┫╰╯┃╭╮┫┃╱╭┫╭╮┃╭┫╭╮┃
┃╰━╯┃┃━┫┃┃┃┃┃┃╰━╯┃╰╯┃┃┃╰╯┃
╰━━━┻━━┻┻┻┻╯╰┻━━━┻━━┻╯╰━━╯""")
root_directory = os.getcwd()
client_directory = os.path.join(root_directory, "Packets/Client")
server_directory = os.path.join(root_directory, "Packets/Server")

def clientDir():
    os.chdir(client_directory)

def serverDir():
    os.chdir(server_directory)

while True:
    menu = input('Command list:\nSend message/dm message - send dm/message \nGet message - get (dm) 100 messages\nJoin server/leave server - join server/leave server\nGo online - go online\nServer list/Channel list/Dm list - get servers/channel list/dm list\nChange about me - change about me\nEnter command: ')
    if menu == 'send message':
        clientDir()
        os.system('python3 send_message.py')
    elif menu == 'get message':
        serverDir()
        os.system('python3 get_message.py')
    elif menu == 'add reaction':
    	clientDir()
    	os.system('python3 reactions.py')
    elif menu == 'join server':
        serverDir()
        os.system('python3 join_server.py')
    elif menu == 'go online':
        clientDir()
        os.system('python3 online.py')
    elif menu == 'dm message':
        clientDir()
        os.system('python3 dm_message.py')
    elif menu == 'leave server':
    	serverDir()
    	os.system('python3 leave_server.py')
    elif menu == "srarki":
    	clientDir()
    	os.system('python3 3.py')
    elif menu == "server list":
        serverDir()
        os.system('python3 get_servers.py')
    elif menu == "channel list":
        serverDir()
        os.system('python3 get_channels.py')
    elif menu == "upload file":
        clientDir()
        os.system('python3 file_upload.py')
    elif menu == "change about me":
        clientDir()
        os.system('python3 change_status.py')
    elif menu == "dm list":
        serverDir()
        os.system('python3 get_dm.py')
    os.chdir(root_directory)
    
    if menu == 'create guild':
        os.chdir(server_directory)
        os.system('python3 create_guild.py')
        os.chdir(root_directory)    
