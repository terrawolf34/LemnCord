import requests, sys; from Utils.Reader import *
sys.path.append("../..")

def edit_message():
    Reader() #token
    headers = {
        "Authorization": token
    }

    # Replace the following with the ID of the channel you want to edit a message in
    channel_id = input("Channel id? ")

    # Replace the following with the ID of the message you want to edit
    message_id = input("MessageID? ")

    # The new content of the message
    new_content = input("edited message content?")

    # Send a PATCH request to the Discord API to edit the message
    response = requests.patch(
        f"https://discord.com/api/v6/channels/{channel_id}/messages/{message_id}",
        headers=headers,
        json={"content": new_content},
    )

    # Check if the request was successful
    if response.status_code == 200:
        print("Message successfully edited")
    else:
        print("Failed to edit message")