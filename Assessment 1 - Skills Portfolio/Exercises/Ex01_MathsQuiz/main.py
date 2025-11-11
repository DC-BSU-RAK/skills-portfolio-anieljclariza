# Make Main Menu Frame and Play Fram

from tkinter import *
import random as rd

main = Tk()

main.geometry("800x600")
main.resizable(0,0)
main.title("Maths Quiz")
main.configure(background="gray")

mainMenuFrame = Frame(main, background="white")

for frame in mainMenuFrame:
    frame.place()

mainMenuButton = Button(mainMenuFrame, text="Main Menu", command=lambda x: switch_frame(mainMenuFrame))
mainMenuButton.place(x=100, y=500, anchor=CENTER)

feedbackLabel = Label(main, text="Welcome")
feedbackLabel.place(x=400, y=225, anchor=CENTER)

displayProblemLabel = Label(main, text="Welcome")
displayProblemLabel.place(x=400, y=250, anchor=CENTER)

displayScoreLabel = Label(main, text="Score: ")
displayScoreLabel.place(x=300, y=300, anchor=CENTER)

correct_answer = None
attempt_count = 0
problem_count = 0
score = 0

def switch_frame(frame):
    frame.tkraise()

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

    displayProblemLabel.config(text=problem)

def isCorrect():
    global attempt_count, score, problem_count
    if int(e1.get()) == correct_answer:
        feedbackLabel.config(text="Correct!", bg="green")
        if attempt_count < 1:
            score += 10
        else:
            score += 5
        displayScoreLabel.config(text=f"Score: {score}")
        attempt_count = 0
        problem_count += 1
        displayProblem()
        
    else:
        feedbackLabel.config(text="Try again", bg="red")
        attempt_count += 1
    
    if attempt_count > 1:
        feedbackLabel.config(text="No Attempts Left!")
        attempt_count = 0
        problem_count += 1
        displayProblem()
    
    if problem_count == 10:
        displayProblemButton.place_forget()
        submitBtn.place_forget()
        displayScoreLabel.config(text=f"Total score: {score}")

e1 = Entry(main)
e1.place(x=400, y=300, anchor=CENTER)

submitBtn = Button(main, text="Submit", command=isCorrect)
submitBtn.place(x=500, y=300, anchor=CENTER)

displayProblemButton = Button(main, text="Display Problem", command=displayProblem)
displayProblemButton.place(x=400, y=350, anchor=CENTER)

switch_frame(mainMenuFrame)

mainloop()