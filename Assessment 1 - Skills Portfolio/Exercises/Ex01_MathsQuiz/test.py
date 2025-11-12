from tkinter import *
import random as rd

main = Tk()
main.geometry("800x600")
main.resizable(0, 0)
main.title("Maths Quiz")
main.configure(background="gray")

# --- Frames ---
mainMenuFrame = Frame(main, background="pink")
playFrame = Frame(main, background="gold")

for frame in (mainMenuFrame, playFrame):
    frame.place(relwidth=1, relheight=1)

# --- Game State Dictionary ---
game = {
    "correct_answer": None,
    "attempt_count": 0,
    "problem_count": 0,
    "score": 0,
    "difficulty": 0
}

# --- Functions ---
def reset_game():
    """Reset all game variables and UI elements."""
    game["correct_answer"] = None
    game["attempt_count"] = 0
    game["problem_count"] = 0
    game["score"] = 0

    feedbackLabel.config(text="Welcome", bg=playFrame["background"])
    displayProblemLabel.config(text="Press 'Display Problem' to start")
    displayScoreLabel.config(text="Score: 0")
    e1.delete(0, END)

    displayProblemButton.place(x=400, y=350, anchor=CENTER)
    submitBtn.place(x=525, y=300, anchor=CENTER)

def switch_frame(frame):
    """Switch frames; reset game when entering play frame."""
    frame.tkraise()
    if frame == playFrame:
        reset_game()

def set_diff(diff, color):
    """Set difficulty, change play frame background, switch to play frame."""
    game["difficulty"] = diff
    playFrame.config(background=color)
    switch_frame(playFrame)

def displayProblem():
    """Generate and display a random math problem based on difficulty."""
    game["correct_answer"] = None
    rdOperator = rd.choice((True, False))

    # Set number range based on difficulty
    if game["difficulty"] == 1:
        rdInt1 = rd.randint(1, 9)
        rdInt2 = rd.randint(1, 9)
    elif game["difficulty"] == 2:
        rdInt1 = rd.randint(1, 99)
        rdInt2 = rd.randint(1, 99)
    else:
        rdInt1 = rd.randint(1, 9999)
        rdInt2 = rd.randint(1, 9999)

    if rdOperator:
        game["correct_answer"] = rdInt1 + rdInt2
        operator = "+"
    else:
        game["correct_answer"] = rdInt1 - rdInt2
        operator = "-"

    problem = f"What is {rdInt1} {operator} {rdInt2}?"
    displayProblemLabel.config(text=problem)
    e1.delete(0, END)  # clear previous entry

def isCorrect():
    """Check user's answer and update score/feedback."""
    try:
        user_answer = int(e1.get())
    except ValueError:
        feedbackLabel.config(text="Please enter a number!", bg="orange")
        return

    if user_answer == game["correct_answer"]:
        feedbackLabel.config(text="Correct!", bg="green")
        if game["attempt_count"] < 1:
            game["score"] += 10
        else:
            game["score"] += 5
        displayScoreLabel.config(text=f"Score: {game['score']}")
        game["attempt_count"] = 0
        game["problem_count"] += 1
        displayProblem()
    else:
        feedbackLabel.config(text="Try again", bg="red")
        game["attempt_count"] += 1

    if game["attempt_count"] > 1:
        feedbackLabel.config(text="No Attempts Left!", bg="orange")
        game["attempt_count"] = 0
        game["problem_count"] += 1
        displayProblem()

    if game["problem_count"] == 10:
        feedbackLabel.config(text="Game Over!", bg="gray")
        displayProblemButton.place_forget()
        submitBtn.place_forget()
        displayScoreLabel.config(text=f"Total score: {game['score']}")

# --- Play Frame Widgets ---
mainMenuButton = Button(playFrame, text="Main Menu", command=lambda: switch_frame(mainMenuFrame))
mainMenuButton.place(x=100, y=500, anchor=CENTER)

feedbackLabel = Label(playFrame, text="Welcome", bg=playFrame["background"])
feedbackLabel.place(x=400, y=225, anchor=CENTER)

displayProblemLabel = Label(playFrame, text="Press 'Display Problem' to start", bg=playFrame["background"])
displayProblemLabel.place(x=400, y=250, anchor=CENTER)

displayScoreLabel = Label(playFrame, text="Score: 0", bg=playFrame["background"])
displayScoreLabel.place(x=275, y=300, anchor=CENTER)

e1 = Entry(playFrame)
e1.place(x=400, y=300, anchor=CENTER)

submitBtn = Button(playFrame, text="Submit", command=isCorrect)
submitBtn.place(x=525, y=300, anchor=CENTER)

displayProblemButton = Button(playFrame, text="Display Problem", command=displayProblem)
displayProblemButton.place(x=400, y=350, anchor=CENTER)

# --- Main Menu Widgets ---
Label(mainMenuFrame, text="Main Menu", bg="pink", font=("Arial", 20)).place(x=400, y=200, anchor=CENTER)

Button(mainMenuFrame, text="Easy", command=lambda: set_diff(1, "green")).place(x=400, y=250, anchor=CENTER)
Button(mainMenuFrame, text="Medium", command=lambda: set_diff(2, "yellow")).place(x=400, y=300, anchor=CENTER)
Button(mainMenuFrame, text="Hard", command=lambda: set_diff(3, "red")).place(x=400, y=350, anchor=CENTER)

# Start on main menu
switch_frame(mainMenuFrame)

mainloop()