clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
import os, sys, json
import inquirer

def start():
    clear()
    # Load profile
    with open('profile.json', 'r') as f:
        profile = json.load(f)
    username = profile['name']

    print('Hello ' + username + ' How can I help you?')
    if profile['inputType'] == 'typing':
        print("""
        Command templates:
        Notify: n time message 
        """)

        
        # Command Start
        print('(n)otify, (q)uit')
        command = input()
        # Quit command
        if command == 'q':
            clear()
            sys.exit()
        # Notify Command
        if command[0] == 'n':
            commandArgs = list(map(str,command.split(' ')))
            notification.message = commandArgs[2]
            notification.send() 
            clear()
            sys.exit()