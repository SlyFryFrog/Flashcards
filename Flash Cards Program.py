# Flash Cards Program
from tkinter.ttk import *
import random
import time
from tkinter import *

app = Tk()

app.title("Flashcards - Made by SlyFryFrog")
app.geometry("800x400")
test = Label(app, text= "Testing")
test.grid(row=8, column=8)

def build_dict():
    dictionary = {}

    # Builds a dictionary from text file and sets everything to lowercase
    with open("verbs.txt", encoding='utf-8') as f:
        for line in f:
            key, val = line.split("; ")
            dictionary[key] = val.strip("\n")

    dictionary =  {key.lower(): val.lower() for key, val in dictionary.items()}
    return dictionary

def flashcard(dictionary):
    reversed_flashcards = input('Do you want your cards given in reverse? (y/n): ')
    reversed_flashcards = reversed_flashcards.lower() == "y"
    get_new_token = True
    while True:
        # Generates a random set of items from dictionary
        if get_new_token == True:
            if reversed_flashcards == True:
                temp = random.choice(list(dictionary.items()))
                current_pair = {1 : temp[0], 0 : temp[1]}
            else:
                current_pair = random.choice(list(dictionary.items()))
            get_new_token = False

        # Displays current_pair and waits for user's input
        print(f'Translate "{current_pair[1]}"')
        user_input = input("Answer here: ").lower()
        if user_input == current_pair[0]:
            print("Correct!\n")
            get_new_token = True
        elif user_input == "exit":
            break

        else:
            print("Please try again.\n")
            get_new_token = False
        
def main():
    dictionary = build_dict()
    flashcard(dictionary)
main()
app.mainloop()
