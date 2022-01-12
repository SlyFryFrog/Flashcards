# Flash Cards Program
import tkinter
import random
import time

# Imports code for gui from another file
import gui

def main():
    while True:
        def flashCard():
            print(f'Translate "{current[1]}"')
            user_input = input("Answer here: ")
            if user_input.lower() == current[0]:
                print("Correct!")
            else:
                print("Please try again.\n")
                flashCard()

        dictionary = {}
        current = ()
        user_input = ""

        # Sets dictionary keys, values as typed in verbs.txt
        with open("verbs.txt") as f:
            for line in f:
                (key, val) = line.split(", ")
                dictionary[key] = val.strip("\n")

        # Converts all text in dictionary to lowercase
        # and sets current to a random key and its matching value
        dictionary =  {key.lower(): val.lower() for key, val in dictionary.items()}
        current = random.choice(list(dictionary.items()))
        print(dictionary)
        

        print(current)
        flashCard()
main()