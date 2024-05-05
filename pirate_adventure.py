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