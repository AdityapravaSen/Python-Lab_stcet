from tkinter import *
from tkinter import messagebox
import tkinter.font
import random


def start_gui():
    global window
    colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]

    index = random.randint(0, 2)

    window = Tk()
    window.title("Color guessing game")
    window.geometry('500x500')

    fonts = tkinter.font.Font(window, family="Anurati Bold")

    heading = Label(
        window, text="WELCOME TO THE COLOR GUESSING GAME 😁", font=fonts)
    heading.grid(column=0, row=0, pady=15)

    subHeading = Label(window, text="Guess the color 🤔", font=("Arial", 15))
    subHeading.grid(column=0, row=1)

    color_names = Label(
        window, text="Choose Between: black,red,green,blue,cyan and yellow 🎯🎯", font=("Arial", 15))
    color_names.grid(column=0, row=2)

    txt = Entry(window, width=35)
    txt.grid(column=0, row=3, padx=5, pady=8)

    label = tkinter.Label(window, font=('Helvetica Bold', 18))
    label.grid(column=0, row=5, pady=8)

    def value():
        if colors[index] == txt.get():
            label.config(text="YOU WIN!!🎉🎊 THE COLOR IS: " +
                         colors[index], fg=colors[index])
        else:
            label.config(text="Sorry, BETTER LUCK NEXT TIME!😔")

    button = Button(window, text="👉CHECK", command=value)
    button.grid(column=0, row=4, pady=4, padx=8)

    replay = Button(window, text="REPLAY🔁", command=refresh)
    replay.grid(column=0, row=7, padx=8)

    window.mainloop()


def refresh():
    window.destroy()
    start_gui()


start_gui()
