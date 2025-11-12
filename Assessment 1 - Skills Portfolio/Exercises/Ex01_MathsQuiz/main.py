# Make Main Menu Frame and Play Frame

from tkinter import *
import random as rd

main = Tk()

main.geometry("800x600")
main.resizable(0,0)
main.title("Maths Quiz")
main.configure(background="gray")

mainMenuFrame = Frame(main, background="pink")
playFrame = Frame(main, background="gold")

for frame in (mainMenuFrame, playFrame):
    frame.place(relwidth=1, relheight=1)

mainMenuButton = Button(playFrame, text="Main Menu", command=lambda: displayMenu(mainMenuFrame))
mainMenuButton.place(x=100, y=500, anchor=CENTER)

feedbackLabel = Label(playFrame, text="Welcome")
feedbackLabel.place(x=400, y=225, anchor=CENTER)

displayProblemLabel = Label(playFrame, text="Welcome")
displayProblemLabel.place(x=400, y=250, anchor=CENTER)

displayScoreLabel = Label(playFrame, text="Score: ")
displayScoreLabel.place(x=275, y=300, anchor=CENTER)

correct_answer = None
attempt_count = 0
problem_count = 0
score = 0
difficulty = 0

def set_diff(diff, color):
    global difficulty
    difficulty = diff
    playFrame.config(background=color)
    displayMenu(playFrame)

def displayMenu(frame):
    frame.tkraise()

def displayProblem():
    global correct_answer
    rdOperator = rd.choice((True, False))

    if difficulty == 1:
        rdInt1 = rd.randint(1, 9)
        rdInt2 = rd.randint(1, 9)    
    elif difficulty == 2:
        rdInt1 = rd.randint(1, 99)
        rdInt2 = rd.randint(1, 99)
    else:
        rdInt1 = rd.randint(1, 9999)
        rdInt2 = rd.randint(1, 9999)

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

e1 = Entry(playFrame)
e1.place(x=400, y=300, anchor=CENTER)

submitBtn = Button(playFrame, text="Submit", command=isCorrect)
submitBtn.place(x=525, y=300, anchor=CENTER)

displayProblemButton = Button(playFrame, text="Display Problem", command=lambda: displayProblem())
displayProblemButton.place(x=400, y=350, anchor=CENTER)

playButton = Button(mainMenuFrame, text="Easy", command=lambda: [displayMenu(playFrame), set_diff(1, "green")])
playButton.place(x=400, y=275, anchor=CENTER)

playButton = Button(mainMenuFrame, text="Medium", command=lambda: [displayMenu(playFrame), set_diff(2, "yellow")])
playButton.place(x=400, y=300, anchor=CENTER)

playButton = Button(mainMenuFrame, text="Hard", command=lambda: [displayMenu(playFrame), set_diff(3, "red")])
playButton.place(x=400, y=325, anchor=CENTER)

displayMenu(mainMenuFrame)

mainloop()