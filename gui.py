from tkinter import *

# Sets default window
window = Tk()
window.geometry('1000x600')
window.title('Flash Cards - Made by SlyFryFrog')

# Adds a button to the gui
btn = Button(window, text = 'Click to begin!', bd = '10', command = window.destroy)
btn.pack(side = 'bottom')

# Title
Label = Label(window, text = 'Welcome to Flash Cards', fg = 'green', bg = 'yellow', relief = 'solid', font = ('arial', 20, 'bold')).pack()

window.mainloop()