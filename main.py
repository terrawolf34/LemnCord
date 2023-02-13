from Packets.Client.sraki import *; from Packets.Client.send_message import *; from Packets.Client.dm_message import *; from Packets.Client.file_upload import *; from Packets.Client.online import *; from Packets.Client.reactions import *;  

from Packets.Server.send_message import *; from Packets.Server.get_channels import *; from Packets.Server.get_message import *; from Packets.Server.get_servers import *; from Packets.Server.join_server import *; from Packets.Server.leave_server import *;
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

while True:
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
