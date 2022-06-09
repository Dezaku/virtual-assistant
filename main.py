import os, sys, json
from setup import firstStart
import inputTypes.typing as typingInput
import inputTypes.list as listInput

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')


# Check if first run
def check():
    if os.path.exists('profile.json'):
        with open('profile.json', 'r') as f:
            profile = json.load(f)
        if profile['inputType'] == 'typing':
            clear()
            typingInput.start()
        elif profile['inputType'] == 'list':
            clear()
            listInput.start()
        else:
            clear()
            print("Hey, it seems like you didn't create your profile yet or your profile is faulty. Please follow the instructions again.")
            firstStart()
    else:
        clear()
        print('It seems like this is your first start. Please follow these instructions:')
        firstStart()


check()