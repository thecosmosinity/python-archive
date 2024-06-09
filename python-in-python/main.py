# Python-In-Python Version 1 by cosmosinity
# This is EXPERIMENTAL SOFTWARE! Expect bugs :)

# Enjoy!

# Importing Modules

import random
import datetime
from time import sleep
import os

# LogOn Screen

print('''


  _____       _   _                     _____             _____       _   _                                                           
 |  __ \     | | | |                   |_   _|           |  __ \     | | | |                                                          
 | |__) |   _| |_| |__   ___  _ __ ______| |  _ __ ______| |__) |   _| |_| |__   ___  _ __                                            
 |  ___/ | | | __| '_ \ / _ \| '_ \______| | | '_ \______|  ___/ | | | __| '_ \ / _ \| '_ \                                           
 | |   | |_| | |_| | | | (_) | | | |    _| |_| | | |     | |   | |_| | |_| | | | (_) | | | |                                          
 |_|    \__, |\__|_| |_|\___/|_| |_|   |_____|_| |_|     |_|    \__, |\__|_| |_|\___/|_| |_|                                          
         __/ |                                                   __/ |                                                                
         |___/                                                   |___/                                                                 
                                                     _       _ _         
                     | |               (_) | | |       / /___ \  | |                                             (_)     (_) |        
  _ __ ___   __ _  __| | ___  __      ___| |_| |__    / /  __) | | |__  _   _    ___ ___  ___ _ __ ___   ___  ___ _ _ __  _| |_ _   _ 
 | '_ ` _ \ / _` |/ _` |/ _ \ \ \ /\ / / | __| '_ \  < <  |__ <  | '_ \| | | |  / __/ _ \/ __| '_ ` _ \ / _ \/ __| | '_ \| | __| | | |
 | | | | | | (_| | (_| |  __/  \ V  V /| | |_| | | |  \ \ ___) | | |_) | |_| | | (_| (_) \__ \ | | | | | (_) \__ \ | | | | | |_| |_| |
 |_| |_| |_|\__,_|\__,_|\___|   \_/\_/ |_|\__|_| |_|   \_\____/  |_.__/ \__, |  \___\___/|___/_| |_| |_|\___/|___/_|_| |_|_|\__|\__, |
                                                                         __/ |                                                   __/ |
                                                                        |___/                                                   |___/ 


''')

print("Please wait while the program loads...")
sleep(random.randint(3, 5))

user = input("Please Input a Username: ")
print("Welcome, " + user + "!")


# Actual Code

global acceptedby

# Code Handler

def handler(pr):
    if pr == 'return':
        x = input("Return?: ")
        print(x)
    if pr == 'do sleep':
        x = input("Timer?: ")
        sleep(int(x))
    if pr == 'credits':
        print('''
        Python-In-Python made by @cosmosinity on YouTube
        GitHub with SOURCE CODE: @thecosmosinity - python-archive
        ''')
    if pr == "date":
        print(datetime.datetime.now())
    if pr == "version" or "ver":
        print("Python-In-Python Version 1.0 by cosmosinity. Made for Command Prompt.")
    else:
        global acceptedby
        acceptedby = 0
def handler2(pr):

    global acceptedby
    if acceptedby == 1:
        
    else:

    if pr == "mkdir" or "make dir" or "makedir":
        directory = input("Dir Name?: ")
        cwd = os.getcwd()
        os.mkdir(os.path.join(cwd, directory))
        print("SUCCESS: Directory " + "'" + directory + "'" + " made in " + cwd)
    if pr == "clear":
        os.system('cls')


# More Credits

'''

Python-In-Python (this is version 1.0) made in 2024 is published and WRITTEN by cosmosinity
Please do not claim this program as your own. If you want to take any source code from this, feel free to do so!

fyi: @thecosmosinity on github
     https://cosmosinity.onrender.com
     subscribe to cosmosinity on YouTube!
     
PS: THIS CODE IS MEANT TO BE RUN ON PYTHON 3.12, RUNNING IT ON VERSIONS ABOVE OR BELOW MAY CAUSE THE CODE TO BREAK!

'''

# Runtime Module

while True:
    p = input(">>> ")
    handler(p)
    handler2(p)
