def Reader():
    txt = open('token.txt', 'r')
    global token
    token = txt.read()