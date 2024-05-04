import random
from time import sleep as wait
import os

choices = ("Yes.", "No.", "It's your choice.", "I can't Decide.", "Maybe, I can't tell.", "No", "ninini", "yessir")

def crash(code):
    print("CRASH! CODE = " + code)
    print("Refer to HELPMANUAL for assistance")
    wait(2)
    exit()


def roll():
    clear()
    ans = random.choice(choices)
    print(ans)


def reroll():
    clear()
    print("Re-rolling...")
    wait(2)
    ans = random.choice(choices)
    print(ans)



clear = lambda: os.system('cls')

input("Welcome to Magic 8 Ball! Press Enter to Play.")
input("What is your question: (yes or no): ")
clear()
roll()

wait(5)

clear()
print("Thank you for playing!")
wait(3)
os.system("taskkill /f /im cmd.exe")
