from tkinter import *
import random as rd

main = Tk()

main.geometry("800x600")
main.resizable(0,0)
main.title("Maths Quiz")
main.configure(background="gray")

correct_answer = None

def displayProblem():
    global correct_answer
    rdOperator = rd.choice((True, False))
    rdInt1 = rd.randint(1, 9)
    rdInt2 = rd.randint(1, 9)

    if rdOperator:
        correct_answer = rdInt1 + rdInt2
        operator = "+"
    else:
        correct_answer = rdInt1 - rdInt2
        operator = "-"

    problem = f"What is {rdInt1} {operator} {rdInt2}?"

    displayProblemLabel = Label(main, text=(problem))
    displayProblemLabel.place(x=400, y=250, anchor=CENTER)

def isCorrect():
    if int(e1.get()) == correct_answer:
        feedback = Label(main, text="Correct!")
        feedback.place(x=300, y=300, anchor=CENTER)
    else:
        feedback = Label(main, text="Incorrect!")
        feedback.place(x=300, y=300, anchor=CENTER)
        

e1 = Entry(main)
e1.place(x=400, y=300, anchor=CENTER)

submitBtn = Button(main, text="Submit", command=isCorrect)
submitBtn.place(x=500, y=300, anchor=CENTER)

displayProblemButton = Button(main, text="Display Problem", command=displayProblem).place(x=400, y=350, anchor=CENTER)

mainloop()