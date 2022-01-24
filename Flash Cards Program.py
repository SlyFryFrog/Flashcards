# Flash Cards Program
from distutils import text_file
import random
import time
from tkinter import *
from functools import partial, partialmethod

# Sets up window
root = Tk()
root.geometry('800x500')
root.title('Flashcards (Alpha) - Made by SlyFryFrog')

# Sets var main_frame defaults
main_frame = Frame(root)
main_frame.pack(side='top', expand=True, fill='both')
main_frame['bg'] = '#009dc4'

reverse_text = Label(text="Reversed (False)")
reverse_text.place(relx=.075, rely=.05, anchor='center')

# Changes current menu to new menu
def change_screen(method, master):
    for widget in master.winfo_children():
        widget.grid_forget()
        widget.destroy()
    method(master)

# Sets screen to main menu
def main_menu(frame):
    Label(frame, text="Main Menu", font=20).place(relx=.5, rely=.05, anchor='center')

    settings_button = Button(frame, text="Settings", command=partial(change_screen, settings_menu, frame))
    settings_button.place(relx=.95, rely=.05, anchor='center')

    start_button = Button(frame, text='START', command=partial(change_screen, pick_screen, frame))
    start_button.place(relx=.5, rely=.5, anchor='center')

# sets screen to settings menu
def settings_menu(frame):
    Label(frame, text="Settings", font=20).place(relx=.5, rely=.05, anchor='center')

    reverse_button = Button(frame, text="Reversed flashcards",command=lambda: reversed_setting(reverse_text))
    reverse_button.place(relx=.5, rely=.2, anchor='center')

    home_button = Button(frame, text="Main Menu", command=partial(change_screen, main_menu, frame))
    home_button.place(relx=.95, rely=.05, anchor='center')

# Enables/disables the reversed setting option
def reversed_setting(reverse_text):
    global reversed_flashcards
    reverse_text.destroy()
    if reversed_flashcards == True:
        reversed_flashcards = False
        
        reverse_text = Label(text="Reversed (False)")
        reverse_text.place(relx=.075, rely=.05, anchor='center')
    else:
        reversed_flashcards = True

        reverse_text = Label(text="Reversed (True)")
        reverse_text.place(relx=.075, rely=.05, anchor='center')

# Creates flashcards
def flashcards(frame):
    global reversed_flashcards
    global dictionary
    global get_new_token

    get_new_token = True

    # Launches the function that creates the flashcards
    Label(frame, text='Flashcard Practice').place(relx=.5, rely=.1, anchor='center')
    
    # Generates a random set of items from dictionary
    cards(frame)

def cards(frame):
    global get_new_token

    # Launches exit_function which clears frame and widgets and builds the main menu frame
    exit_button = Button(frame, text='Exit', command=lambda: exit_function(frame))
    exit_button.place(relx=.9, rely=.9, anchor='center')
    
    answer_textbox = Entry(frame, text='')
    answer_textbox.place(relx=.5, rely=.8, anchor='center')

    # Checks flashcard token
    if get_new_token == True:
        if reversed_flashcards == True:
            temp = random.choice(list(dictionary.items()))
            current_pair = {1 : temp[0], 0 : temp[1]}

        else:
            current_pair = random.choice(list(dictionary.items()))

        get_new_token = False
    # Displays what it wants the user to translate
    translate_this_text = Label(text=f'Translate "{current_pair[1]}"')
    translate_this_text.place(relx=.5, rely=.5, anchor='center')

    # Checks user input to see if it matches the meaning of the flashcard or not
    def sumbit_answer(answer_textbox):
        global get_new_token

        user_input = answer_textbox.get()

        if user_input == current_pair[0]:
            translate_this_text.destroy()

            get_new_token = True
            cards(frame)
                    
        else:
            get_new_token = False
    # Launches functions to check if submition is correct
    submit_button = Button(frame, text='Submit', command= lambda: sumbit_answer(answer_textbox))
    submit_button.place(relx=.5, rely=.9, anchor='center')

    # Destroys old frame and widgets and launches other function to create new main menu frame
    def exit_function(frame):
        change_screen(main_menu, frame)
        translate_this_text.destroy()

def pick_screen(frame):
    def destroy():
        build_dict()
        return change_screen(flashcards, frame)

    def verbs():
        global text_file
        text_file = 'verbs.txt'
        return destroy()

    verbs_button = Button(frame, text='Verbs', command=verbs)
    verbs_button.place(relx=.5, rely=.5, anchor='center')

    def nouns():
        global text_file
        text_file = 'nouns.txt'
        return destroy()
    
    nouns_button = Button(frame, text='Nouns', command=nouns)
    nouns_button.place(relx=.3, rely=.5, anchor='center')

# Builds dictionary
def build_dict():
    global dictionary
    global text_file
    dictionary = {}

    # Builds a dictionary from text file and sets everything to lowercase
    with open(text_file, encoding='utf-8') as file:
        for line in file:
            key, val = line.split("; ")
            dictionary[key] = val.strip("\n")

    dictionary =  {key.lower(): val.lower() for key, val in dictionary.items()}

# Launches starting functions and sets global variables
main_menu(main_frame)
global reversed_flashcards
reversed_flashcards = False 
root.mainloop()