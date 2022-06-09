import os, sys, re, json
import inquirer
from notifypy import Notify


# Load Profile
with open('profile.json', 'r') as f:
            profile = json.load(f)

# Default Notification Preset
notification = Notify(
      default_notification_title="Virtual Assistant",
      default_notification_icon="./assets/icon.png",
)
def start():

    print("""
        Command templates:
        Notify: n time message 
        Quit: q
        """)
    command = inquirer.text(message='Hello ' + profile['name'] + '! How can I help you?')
    if command[0] == 'n':
        commandArgs = list(map(str,command.split(' ')))
        notification.message = str(commandArgs[2:])
        notification.send()
