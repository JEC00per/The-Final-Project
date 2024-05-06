import time
import random

# Define global variables
crew = ["Captain Blackbeard", "First Mate Shaw", "Navigator Boone", "Cookhouse Jack", "Gunnery Sergeant Clay"]

# Introduction to the game
def introduction():
    print("Avast, me hearty crew!")
    print("I'm Captain Blackbeard, captain of the Jolly Roger, and I seek the treasure lost to time!")
    print("Chart a course, men! We're going on a treasure hunt!")

def choose_path():
    print("\nLay anchor! We've come to a crossroads!")
    print("There be two paths before us. Which one shall we take?")
    print("1. Sail through the Devil's Triangle.")
    print("2. Head ashore to investigate the seedy Smuggler's Cove.")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        devil_triangle()
    elif choice == '2':
        smugglers_cove()
    else:
        print("Invalid choice. Try again.")
        choose_path()

# Function for the Stormy Seas path
def devil_triangle():
    print("\nYe scallywags ready the ship as we set sail into the Devil's Triangle!")
    print("The waves be crashing against the hull, and the wrath of sea is upon us!")

    time.sleep(2)

    print("\nThe sea opens its mouth, a fierce whirlpool descends on our vessel!")

    time.sleep(2)

    print("\nBatten down the hatches and keep the ship afloat!")

    time.sleep(2)

    success_chance = 0.5  # 50% chance of success
    if random.random() < success_chance:
        print("\nYe've navigated the stormy seas skillfully, mates! Resume our course towards the treasure!")
        treasure_awaits()
    else:
        print("\nShe's beginning to flood, the Devil has come from his den to claim us!")
        print("The sea be a cruel master, but we live to fight another day. May our shipwrecked souls find luck.")

# Function for the Pirate Cove path
def smugglers_cove():
    print("\nWe've anchored at Pirate Cove, a haven for scoundrels and thieves!")
    print("The cove be shrouded in mist, and danger lurks around every corner.")

    time.sleep(2)

    print("\nWe must be cautious as we explore the cove. Who knows what secrets it holds?")

    time.sleep(2)

    encounter_chance = 0.7  # 70% chance of encountering pirates
    if random.random() < encounter_chance:
        print("\nScoundrels strike from the shadows, men! Draw your swords!")
        print("Prepare for a brawl, ye scurvy dogs!")
        combat()
    else:
        print("\nThe coast be clear, our contacts in the cove come in handy at last!")
        treasure_awaits()