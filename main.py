# import
import sys
import time
import random as r
import inquirer
import re
import keyboard

# variables
health = 10
hunger = 10
health_max = 10
hunger_max = 10
backpack = []
locations = [
    "forest",
    "cave",
    "desert",
    "mountain",
    "village",
    "castle",
    "home",
]


# functions
def go(location, time):
    if location in locations:
        print("You are walking to " + location + ".")
        time.sleep(time)
        print("You arrived at " + location + ".")
    else:
        print("\"" + location + "\""
              " is not a known location.")


# real code
print("WATCHER: exec main.py")
time.sleep(0.3)
print("loading dependecies...")
time.sleep(0.9)
print("loading modules...")
time.sleep(1.2)
print("main.py: start file main.py")
time.sleep(0.3)
print('''C:\\survive\\main.py: welcome to \n
████████████████████████████████████████████████████████████████
███████████████████████████████████████  ███████████████████████
██     ██   ██   █  █    █   █████   █████   █████   ████   ████
█   █████   ██   ██   █████   ███   ██   ██   ███   ███  ███   █
███    ██   ██   ██   ██████   █   ███   ███   █   ███         █
█████   █   ██   ██   ███████     ████   ████     ████  ████████
█      ████      █    ████████   █████   █████   ███████     ███
████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████
ƀɏ @ꝁɨnđƻƻ3ƻ''')
username = input("Please enter your name: ")
ynPrompt = [
    inquirer.List(
        "yn",
        message="Do you want to play as \"" + username + "\"?",
        choices=["Yes", "No"],
    )
]
ynAns = inquirer.prompt(ynPrompt)
if ynAns["yn"] == "Yes":
    print("Welcome to Survive, " + username + "!")
else:
    print("Ok, you'll have to restart the program to choose a different name.")
    sys.exit()
tutPrompt = [
    inquirer.List("tutorial",
                  message="Would you like to see the prolouge?",
                  choices=["See Prolouge", "Skip Prolouge"])
]
tutAns = inquirer.prompt(tutPrompt)
if tutAns is not None and tutAns["tutorial"] == "See Prolouge":
    print("You wake up in a forest.")
    time.sleep(1.2)
    print("You look around and see a path leading north.")
    time.sleep(1.2)
    print("As you are walking, you see a village nearby.")
    time.sleep(1.2)
    print("Villager: Hey, where did you come from?")
    time.sleep(1.2)
    print(
        "You: Um... I don't know. I woke up in the forest and found this place."
    )
    time.sleep(1)
    print("Villager: Woah. What's your name?")
    time.sleep(1)
    print(username, ". What about you?")
    time.sleep(1)
    print("Villager: I'm Jack.")
    time.sleep(1)
    print("Jack: How about I show you around?")
    time.sleep(1)
    print("You: Yeah, let's go.")
    time.sleep(1)
    print("You and Jack walk to the plaza.")
    time.sleep(1)
    print("Jack: So!")
    time.sleep(1)
    print("Jack: This is the plaza, where all of the stuff happens.")
    time.sleep(1)
