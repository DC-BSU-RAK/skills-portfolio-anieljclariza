from tkinter import *
import random as rd
from PIL import Image, ImageTk

main = Tk()
main.geometry("800x600")
main.resizable(0,0)
main.title("Maths Quiz")

background_image = Image.open(r"Assessment 1 - Skills Portfolio\Exercises\Ex01_MathsQuiz\mainMenu.jpg")
background_image = background_image.resize((800, 600))
background_photo = ImageTk.PhotoImage(background_image)

easyDiffBackground = Image.open( r"Assessment 1 - Skills Portfolio\Exercises\Ex01_MathsQuiz\1.jpg")
easyDiffBackground = easyDiffBackground.resize((800, 600))
easyDiffPhoto = ImageTk.PhotoImage(easyDiffBackground)

medDiffBackground = Image.open( r"Assessment 1 - Skills Portfolio\Exercises\Ex01_MathsQuiz\2.jpg")
medDiffBackground = medDiffBackground.resize((800, 600))
medDiffPhoto = ImageTk.PhotoImage(medDiffBackground)

hardDiffBackground = Image.open( r"Assessment 1 - Skills Portfolio\Exercises\Ex01_MathsQuiz\3.jpg")
hardDiffBackground = hardDiffBackground.resize((800, 600))
hardDiffPhoto = ImageTk.PhotoImage(hardDiffBackground)

# Frames ---
mainMenuFrame = Frame(main)
playFrame = Frame(main, background="pink")

for frame in (mainMenuFrame, playFrame):
    frame.place(relwidth=1, relheight=1)

# <--- Game State --->
game = {
    "correct_answer": "",
    "attempt_count": 0,
    "question_number": 1,
    "score": 0,
    "difficulty": 0
}

# <--- Functions --->

def switch_frame(frame):
    frame.tkraise()

def reset_game():
    game["correct_answer"] = ""
    game["attempt_count"] = 0
    game["question_number"] = 1
    game["difficulty"] = 0

    feedbackLabel.config(text="Welcome!")

    displayProblemLabel.config(text="Press 'Display Problem' to start")

    displayScoreLabel.config(text="Question Number: 1")
    answerEntry.delete(0, END)

    displayProblemButton.place(x=400, y=350, anchor=CENTER)
    submitButton.place(x=525, y=300, anchor=CENTER)

def set_diff(diff, color):
    game["difficulty"] = int(diff)
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
    displayProblemLabel.config(text=problem, font=("Arial", 16, "bold"))
    answerEntry.delete(0, END)

def is_correct():
    try:
        user_answer = int(answerEntry.get())
    except ValueError:
        feedbackLabel.config(text="Please enter a number!", bg="orange")
        return
    
    if user_answer == game["correct_answer"]:
        feedbackLabel.config(text="Correct✅!")
        if game["attempt_count"] < 1:
            game["score"] += 10
        else:
            game["score"] += 5
        
        game["question_number"] += 1
        displayScoreLabel.config(text=f"Question Number: {game['question_number']}")
        display_problem()
    else:
        feedbackLabel.config(text="Try again🔄")
        game["attempt_count"] += 1
    
    if game["attempt_count"] > 1:
        feedbackLabel.config(text="No Attempts Left!", background="orange")
        game["attempt_count"] = 0
        game["question_number"] += 1
        displayScoreLabel.config(text=f"Question Number: {game['question_number']}")
        display_problem()

    if game["question_number"] == 11:
        feedbackLabel.config(text="Game Over!", background="gray")
        displayProblemButton.place_forget()
        submitButton.place_forget()
        displayScoreLabel.config(text=f"Total Score: {game['score']}")
        displayProblemLabel.config(text="Thanks for trying out my program!")
        mainMenuButton.config(text="Play Again or Exit")

def change_background(diff):
    if diff == 1:
        playFrameBackground.config(image=easyDiffPhoto)
    elif diff == 2:
        playFrameBackground.config(image=medDiffPhoto)
    else:
        playFrameBackground.config(image=hardDiffPhoto)

# <--- Play Frame Widgets --->
playFrameBackground = Label(playFrame)
playFrameBackground.place(x=0, y=0, relwidth=1, relheight=1)

mainMenuButton = Button(playFrame, text="Main Menu", command=lambda: [switch_frame(mainMenuFrame), reset_game()])
mainMenuButton.place(x=400, y=500, anchor=CENTER)

feedbackLabel = Label(playFrame, text="Welcome to my Maths Quiz!", background=playFrame["background"])
feedbackLabel.place(x=400, y=225, anchor=CENTER)

displayProblemLabel = Label(playFrame, text='Press "Display Problem" to start', background=playFrame["background"])
displayProblemLabel.place(x=400, y=250, anchor=CENTER)

displayScoreLabel = Label(playFrame, text="Question Number: 1", background=playFrame["background"])
displayScoreLabel.place(x=275, y=300, anchor=CENTER)

answerEntry = Entry(playFrame)
answerEntry.place(x=400, y=300, anchor=CENTER)

submitButton = Button(playFrame, text="Submit", command=is_correct)
submitButton.place(x=525, y=300, anchor=CENTER)

displayProblemButton = Button(playFrame, text="Display Problem", command=display_problem)
displayProblemButton.place(x=400, y=350, anchor=CENTER)

# <--- Main Menu Frame Widgets --->
backGroundLabel = Label(mainMenuFrame, image=background_photo)
backGroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

easyButton = Button(mainMenuFrame, text="Easy", command=lambda: [switch_frame(playFrame), set_diff(1, "green"), change_background(1)])
easyButton.place(x=400, y=270, anchor=CENTER)

mediumButton = Button(mainMenuFrame, text="Medium", command=lambda: [switch_frame(playFrame), set_diff(2, "orange"), change_background(2)])
mediumButton.place(x=400, y=300, anchor=CENTER)

hardButton = Button(mainMenuFrame, text="Hard", command=lambda: [switch_frame(playFrame), set_diff(3, "red"), change_background(3)])
hardButton.place(x=400, y=330, anchor=CENTER)

quitButton = Button(mainMenuFrame, text="Quit", command=lambda: exit())
quitButton.place(x=400, y=360, anchor=CENTER)

# Start on Main Menu
switch_frame(mainMenuFrame)

mainloop()