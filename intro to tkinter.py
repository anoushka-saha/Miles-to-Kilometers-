#Anoushka Saha
#Day 27 Practice
#Intro to Tkinter
#July 1st, 2024

#Importing like this allows us to get rid of all module mentions
from tkinter import *

#New window using Tk class
window = Tk()

#Changing title of window
window.title("My First GUI Program")

#Setting size of window
window.minsize(width = 500, height = 300)

#Initializing label with text
my_label = Label(text = "I am a label", font = ("Arial", 24, "bold"))

#Displaying label on screen
#Side = "left", "right", "top", "bottom" --> Centers text on that side of screen
#Expand = True --> Centers text in the middle of screen
my_label.pack()

#How to configure and change/update properties of previously created component
my_label["text"] = "New Text"
my_label.config(text = "New Text")

#Button
def button_clicked():
    my_label["text"] = input.get()
    my_label.config(text = input.get())

my_button = Button(text = "Click Me", command = button_clicked)
my_button.pack()

#Entry: Taking input from user on screen
input = Entry(width = 10)
input.pack()

#Returns entry as string
input.get()



#Keeping the window open on screen, always at end of program
window.mainloop()