## import everything from the tkinter toolkit to use for this exercise
from tkinter import *
import random as rd

main = Tk()
main.geometry('800x800')
main.resizable(0,0)

mainMenu = Frame(main)
easyFrame = Frame(main, bg='green')
mediumFrame = Frame(main, bg='yellow')

for frame in (mainMenu, easyFrame, mediumFrame):
    frame.place(width=800, height=600)

title = Label(mainMenu, text="Maths Quiz", font=('Arial', 25))
title.place(x=400,y=100, anchor=CENTER)

programmer = Label(mainMenu, text="by Aniel-J Clariza :)", font=('Arial', 15))
programmer.place(x=400, y=150, anchor=CENTER)

def switch_frame(frame):    
    frame.tkraise()

easyModeButton = Button(mainMenu, text="Easy Difficulty", font=('', 15), bg='green', activebackground='lightgreen', command=lambda: switch_frame(easyFrame))
easyModeButton.place(x=400, y=225, anchor=CENTER)

mainMenuButton = Button(main, text='Main Menu', command=lambda: switch_frame(mainMenu))
mainMenuButton.place(x=400, y=700, anchor=CENTER)

randomIntEasy1 = rd.randint(1,9)
randomIntEasy2 = rd.randint(1,9)
randomOperator = rd.choice(('+', '-'))

problem = (f"{randomIntEasy1} {randomOperator} {randomIntEasy2}")

easyQuestion = Label(easyFrame, text=f"What is {problem}?")
easyQuestion.place(x=400, y=200, anchor=CENTER)

e1 = Entry(easyFrame)
e1.place(x=400, y=300, anchor=CENTER)

submitButton = Button(easyFrame)

"""
mediumModeButton = Button(mainMenu, text="Medium Difficulty", font=('', 15), bg='yellow', activebackground='lightyellow', command=lambda:switch_frame(mediumFrame))
mediumModeButton.place(x=400, y=300, anchor=CENTER)

mainMenuButton2 = Button(mediumFrame, text='Back to Main Menu', command=lambda: switch_frame(mainMenu))
mainMenuButton2.place(x=400, y=500, anchor=CENTER)


hardMode = Button(main, text="Hard Difficulty", font=('', 15), bg='red', activebackground='pink')
hardMode.place(x=400, y=375, anchor=CENTER)
"""

switch_frame(mainMenu)

main.mainloop()