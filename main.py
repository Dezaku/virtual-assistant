import os
import json

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')


def firstStart():
    clear()
    # create profile.json
    data = {}
    username=input("Hey, I don't know you. What's your name?")
    data['name'] = username
    print(data)
    data['inputType'] = 'none'
    inputType=input('Hello ' + username + ' which input type do you want to use, (l)ist or (t)yping?')
    print(data)
    while data['inputType'] == 'none':
        if inputType == 'l':
            data['inputType'] = 'list'
        elif inputType == 't':
            data['inputType'] = 'typing'
        else: 
            inputType = input('Please use "l" for list or "t" for typing')
        print(data)
    with open('profile.json', 'w') as outfile:
        json.dump(data, outfile)
    start()
# normal startup
def start():
    clear()
    with open('profile.json', 'r') as f:
        profile = json.load(f)
    username = profile['name']
    print('Hello ' + username + ' How can I help you?')
    if profile['inputType'] == 'typing':
        print('(n)otify, ')

# Check if first run
if os.path.exists('profile.json'):
    start()
else:
        firstStart()