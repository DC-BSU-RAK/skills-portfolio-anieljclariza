from tkinter import *
import random as rd

main = Tk()
main.geometry("800x600")
main.resizable(0,0)
main.title("Maths Quiz")

mainMenuFrame = Frame(main, background="white")
playFrame = Frame(main, background="pink")

for frame in (mainMenuFrame, playFrame):
    frame.place(relwidth=1, relheight=1)

# This is the displayMenu, but with added features
def switchFrame(frame):
    frame.tkraise()

easyButton = Button(mainMenuFrame, text="Easy")
easyButton.place(x=400, y=270, anchor=CENTER)

mediumButton = Button(mainMenuFrame, text="Medium")
mediumButton.place(x=400, y=300, anchor=CENTER)

hardButton = Button(mainMenuFrame, text="Hard")
hardButton.place(x=400, y=330, anchor=CENTER)

switchFrame(mainMenuFrame)

mainloop()