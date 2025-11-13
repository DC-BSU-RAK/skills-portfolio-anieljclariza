from tkinter import *
import random as rd

main = Tk()
main.geometry("800x600")
main.resizable(0,0)
main.title("Maths Quiz")

# Frames ---
mainMenuFrame = Frame(main, background="white")
playFrame = Frame(main, background="pink")

for frame in (mainMenuFrame, playFrame):
    frame.place(relwidth=1, relheight=1)

# <--- Game State --->
game = {
    "correct_answer": "",
    "attempt_count": 0,
    "question_number": 0,
    "score": 0,
    "difficulty": 0
}

# <--- Functions --->

def switch_frame(frame):
    frame.tkraise()

def reset_game():
    game["correct_answer"] = ""
    game["attempt_count"] = 0
    game["question_number"] = 0
    game["difficulty"] = 0
    game["difficulty"] = 0

def set_diff(diff, color):
    game["difficulty"] = diff
    playFrame.config(background=color)

def display_problem():
    rdOperator = rd.choice((True, False))

    if game["difficulty"] == 1:
        rdInt1 = rd.randint(1, 9)
        rdInt2 = rd.randint(1, 9)
    elif game["difficulty"] == 2:
        rdInt1 = rd.randint(10, 99)
        rdInt2 = rd.randint(10, 99)
    else:
        rdInt1 = rd.randint(1000, 9999)
        rdInt2 = rd.randint(1000, 9999)
    
    if rdOperator:
        rdOperator = '+'
        game["correct_answer"] = rdInt1 + rdInt2
    else:
        rdOperator = '-'
        game["correct_answer"] = rdInt1 - rdInt2
    
    problem = f"What is {rdInt1} {rdOperator} {rdInt2}"
    displayProblemLabel.config(text=problem)
    answerEntry.delete(0, END)

def is_correct():
    try:
        user_answer = int(answerEntry.get())
    except ValueError:
        feedbackLabel.config(text="Please enter a number!", bg="orange")
        return
    
    if user_answer == game["correct_answer"]:

# Play Frame Widgets

mainMenuButton = Button(playFrame, text="Main Menu")

# Main Menu Frame Widgets
easyButton = Button(mainMenuFrame, text="Easy", command=lambda: switch_frame(playFrame))
easyButton.place(x=400, y=270, anchor=CENTER)

mediumButton = Button(mainMenuFrame, text="Medium")
mediumButton.place(x=400, y=300, anchor=CENTER)

hardButton = Button(mainMenuFrame, text="Hard")
hardButton.place(x=400, y=330, anchor=CENTER)

quitButton = Button(mainMenuFrame, text="Quit", command=lambda: exit())
quitButton.place(x=400, y=360, anchor=CENTER)

switch_frame(mainMenuFrame)

mainloop()