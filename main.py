from Packets.Client.sraki import *; from Packets.Client.change_status import *; from Packets.Client.send_message import *; from Packets.Client.dm_message import *; from Packets.Client.file_upload import *; from Packets.Client.online import *; from Packets.Client.reactions import *;  

from Packets.Server.get_dm import *; from Packets.Server.send_message import *; from Packets.Server.get_channels import *; from Packets.Server.get_message import *; from Packets.Server.get_servers import *; from Packets.Server.join_server import *; from Packets.Server.leave_server import *;
print("""╭╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╭╮
┃┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱┃┃
┃┃╱╱╭━━┳╮╭┳━╮┃┃╱╰╋━━┳━┳━╯┃
┃┃╱╭┫┃━┫╰╯┃╭╮┫┃╱╭┫╭╮┃╭┫╭╮┃
┃╰━╯┃┃━┫┃┃┃┃┃┃╰━╯┃╰╯┃┃┃╰╯┃
╰━━━┻━━┻┻┻┻╯╰┻━━━┻━━┻╯╰━━╯""")

while True:
    menu = input('Command list:\nSend message/dm messagee - send dm/message \nGet message - get 100 messages\nJoin server/leave server - join server/leave server\nGo online - go online\nServer list/Channel list - get servers/channel list\nupload file - upload file\n>>> Enter command: ')
    if menu == 'send message':
        send_message_client()  

    elif menu == 'get message':
        get_message()

    elif menu == 'add reaction':
        reactions()

    elif menu == 'join server':
        join_server()

    elif menu == 'go online':
        online()

    elif menu == 'dm message':
        dm_message()

    elif menu == 'leave server':
        leave_server()

    elif menu == 'srarki':
        sraki()

    elif menu == 'server list':
        get_servers()

    elif menu == 'channel list':
        get_channels()

    elif menu == 'upload file':
        file_upload()

    elif menu == 'change status':
        change_status()

    elif menu == 'dm list':
        get_dm()