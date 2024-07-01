#Anoushka Saha
#Day 27 Practice
#Intro to Tkinter
#July 1st, 2024

import tkinter

#New window using Tk class
window = tkinter.Tk()

#Changing title of window
window.title("My First GUI Program")

#Setting size of window
window.minsize(width = 500, height = 300)

#Initializing label with text
my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))

#Displaying label on screen
#Side = "left", "right", "top", "bottom" --> Centers text on that side of screen
#Expand = True --> Centers text in the middle of screen
my_label.pack(side = "left")

#Keeping the window open on screen, always at end of program
window.mainloop()