import os

print("""
╭╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╭╮
┃┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱┃┃
┃┃╱╱╭━━┳╮╭┳━╮┃┃╱╰╋━━┳━┳━╯┃
┃┃╱╭┫┃━┫╰╯┃╭╮┫┃╱╭┫╭╮┃╭┫╭╮┃
┃╰━╯┃┃━┫┃┃┃┃┃┃╰━╯┃╰╯┃┃┃╰╯┃
╰━━━┻━━┻┻┻┻╯╰┻━━━┻━━┻╯╰━━╯
""")
root_directory = os.getcwd()
client_directory = os.path.join(root_directory, "Packets/Client")
server_directory = os.path.join(root_directory, "Packets/Server")

while True:
    menu = input('Command list:\nSend message - send message \nGet message - get 100 messages\nJoin server - join server\nGo online - go online\nDm message - send dm\nLeave server - leave server\nEnter command: ')
    if menu == 'send message':
        os.chdir(client_directory)
        os.system('python3 send_message.py')
        os.chdir(root_directory)
    
    if menu == 'get message':
        os.chdir(server_directory)
        os.system('python3 get_message.py')
        os.chdir(root_directory)
        
    if menu == 'add reaction':
    	os.chdir(client_directory)
    	os.system('python3 reactions.py')
    	os.chdir(root_directory)
        
    if menu == 'join server':
        os.chdir(server_directory)
        os.system('python3 join_server.py')
        os.chdir(root_directory)
        
    if menu == 'go online':
        os.chdir(client_directory)
        os.system('python3 online.py')
        os.chdir(root_directory)
        
    if menu == 'dm message':
        os.chdir(client_directory)
        os.system('python3 dm_message.py')
        os.chdir(root_directory)
        
    if menu == 'leave server':
    	os.chdir(server_directory)
    	os.system('python3 leave_server.py')
    	os.chdir(root_directory)
    	
    	
    if menu == "srarki":
    	os.chdir(client_directory)
    	os.system('python3 3.py')
    	os.chdir(root_directory)
  
