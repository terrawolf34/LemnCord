import requests, sys; from Utils.Reader import *
sys.path.append("../..")

def file_upload():
    Reader() #token
    
    
    headers = {
        "Authorization": token
    }
    
    def upload_file(channel_id, file_path):
        files = {"file": open(file_path, "rb")}
        response = requests.post(f"https://discord.com/api/v6/channels/{channel_id}/messages", headers=headers, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    channel_id = input("Enter the ID of the channel you want to upload a file to: ")
    file_path = input("Enter the path of the file you want to upload: ")
    response = upload_file(channel_id, file_path)
    if response:
        print("File uploaded successfully!")
    else:
        print("Could not upload file. Check your token and try again.")
    