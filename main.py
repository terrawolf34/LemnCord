<<<<<<< HEAD:main.py
from Packets.Client.sraki import *; from Packets.Client.send_message import *; from Packets.Client.dm_message import *; from Packets.Client.file_upload import *; from Packets.Client.online import *; from Packets.Client.reactions import *;  

from Packets.Server.send_message import *; from Packets.Server.get_channels import *; from Packets.Server.get_message import *; from Packets.Server.get_servers import *; from Packets.Server.join_server import *; from Packets.Server.leave_server import *;
=======
import os
>>>>>>> bc2cc1bdd6ede145e5564283ebcb07cc79682239:menu.py

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
<<<<<<< HEAD:main.py
    menu = input('Command list:\nSend message/dm messagee - send dm/message \nGet message - get 100 messages\nJoin server/leave server - join server/leave server\nGo online - go online\nServer list/Channel list - get servers/channel list\nupload file - upload file\n>>> Enter command: ')
    if menu == 'send message':
        send_message_client()  
        
    if menu == 'get message':
        get_message()
            
    if menu == 'add reaction':
        reactions()
        
    if menu == 'join server':
        join_server()
        
    if menu == 'go online':
        online()
        
    if menu == 'dm message':
        dm_message()
        
    if menu == 'leave server':
        leave_server()
        
        
    if menu == "srarki":
        sraki()
        
    
    if menu == "server list":
        get_servers()
        
        
    if menu == "channel list":
        get_channels()
        
    if menu == "upload file":
        file_upload()

#fixed by loxotron from 97 team
=======
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
>>>>>>> bc2cc1bdd6ede145e5564283ebcb07cc79682239:menu.py
