import random
from tkinter import *
import random

root = Tk()

root.title("RNG Colour")

root.geometry("400x400")



## ["","","","","","", "",""]

colors = {
    "q1":"maroon1",
    "q2":"lawn green",
    "q3":"magenta2",
    "q4":"purple1",
    "q5":"springgreen2",
    "q6":"chocolate1",
    "q7":"deep pink",
    "q8":"cyan",
}


def rngColor():

    colours = random.randint(1, 8)
    root.configure(background = colors["q" + str(colours)])
    

button = Button(root, text="Change Bg", command=rngColor)

button. place(relx = 0.5 , rely =0.5 , anchor = CENTER)

root.mainloop()