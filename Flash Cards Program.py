# Flash Cards Program
from os import remove
import tkinter
import random
import time

# Imports code for gui from another file
import gui

def build_dict():
    dictionary = {}

    # Builds a dictionary from text file and sets everything to lowercase
    with open("verbs.txt") as f:
        for line in f:
            (key, val) = line.split(", ")
            dictionary[key] = val.strip("\n")
    dictionary =  {key.lower(): val.lower() for key, val in dictionary.items()}
    return dictionary

def flashcard(dictionary):
    print('Type "exit" to exit the program.')

    while True:

        # Generates a random set of items from dictionary
        current_pair = random.choice(list(dictionary.items()))

        print(f'Translate "{current_pair[1]}"')

        user_input = input("Answer here: ")
        if user_input.lower() == current_pair[0]:
            print("Correct!\n")
        elif user_input.lower() == "exit":
            break
        else:
            print("Please try again.\n")


def main():
    dictionary = build_dict()
    flashcard(dictionary)

main()
