# Import necessities for program to work.
    # tkinter for GUI
    # random for random integer values
    # PIL for placing a background image
from tkinter import *
import random as rd
from PIL import Image, ImageTk

# Main tkinter window creation
main = Tk()
main.geometry("800x600")
main.resizable(0,0)
main.title("Maths Quiz")

# Background images to be used every frame and difficulty: Main Menu and Easy to Hard difficulties
background_image = Image.open(r"Assessment 1 - Skills Portfolio\Exercises\Ex01_MathsQuiz\mainMenu.jpg") # Opens the image file
background_image = background_image.resize((800, 600)) # Resize to window size
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

# Main Menu Frame and Play Frame to be used later
mainMenuFrame = Frame(main)
playFrame = Frame(main, background="pink")

# Place each frame and fill the whole window
for frame in (mainMenuFrame, playFrame):
    frame.place(relwidth=1, relheight=1)

# < --- Game Stats --- >
# This is the game stats dictionary for storing stats like the correct answer, number of attempts, question, etc.
    # Used to modify the stats easier than using global variables in my opinion
game = {
    "correct_answer": "",
    "attempt_count": 0,
    "question_number": 1,
    "score": 0,
    "difficulty": 0
}

# <--- Functions --->

    # Used for switching between main menu frame and play frame
def switch_frame(frame):
    frame.tkraise()

    # Resets the game stats to default every time the user goes back to the main menu
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

    # Sets the game difficulty according to the difficulty the user chose from the main menu
def set_diff(diff):
    game["difficulty"] = int(diff)

    # Displays the problem when the "Display Problem" button is clicked
def display_problem():

        # Uses if-elif-else for diffrent difficulties based from the value in the game[] dictionary; 1 digit for easy, 2 digits for medium, and 4 digits for hard
    if game["difficulty"] == 1:
        rdInt1 = rd.randint(1, 9)
        rdInt2 = rd.randint(1, 9)
    elif game["difficulty"] == 2:
        rdInt1 = rd.randint(10, 99)
        rdInt2 = rd.randint(10, 99)
    else:
        rdInt1 = rd.randint(1000, 9999)
        rdInt2 = rd.randint(1000, 9999)
    
    # Randomly chooses between True or False, where True means '+' operator and False a '-' operator
    rdOperator = rd.choice((True, False))
        # Add or subtract the two integer values based on the rdOperator
    if rdOperator:
        rdOperator = '+'
        game["correct_answer"] = rdInt1 + rdInt2
    else:
        rdOperator = '-'
        game["correct_answer"] = rdInt1 - rdInt2
    
    # Displays the problem on the ProblemLabel created and make more changes to make text more readable
    problem = f"What is {rdInt1} {rdOperator} {rdInt2}"
    displayProblemLabel.config(text=problem, font=("Arial", 16, "bold"))

    # Deletes the values, if any, in the answerEntry Entry field for a cleaner field
    answerEntry.delete(0, END)

# Checks whether the value in the entry field is correct, incorrect, or has ValueError
def is_correct():
    try:
        user_answer = int(answerEntry.get())
    except ValueError:
        feedbackLabel.config(text="Please enter a number!", background="orange")
        return
    
    # Gives feedback if answer is correct and gives the appropriate score relative to the number of attempts used where 10 is awarded on first try and 5 for the second
    if user_answer == game["correct_answer"]:
        feedbackLabel.config(text="Correct✅!")
        if game["attempt_count"] < 1:
            game["score"] += 10
        else:
            game["score"] += 5
        
        # Moves to the next question if answer is correct
        game["question_number"] += 1
        displayScoreLabel.config(text=f"Question Number: {game['question_number']}")
        display_problem()

        # Gives feedback if answer is wrong and increments the attempt count
    else:
        feedbackLabel.config(text="Try again🔄")
        game["attempt_count"] += 1
    
        # Gives feedback telling the user that they have no attempts left and then resets the attempt count and moves on to the next question
    if game["attempt_count"] > 1:
        feedbackLabel.config(text="No Attempts Left!", background="orange")
        game["attempt_count"] = 0
        game["question_number"] += 1
        displayScoreLabel.config(text=f"Question Number: {game['question_number']}")
        display_problem()

        # If all 10 questions are answered, displays "game over screen", score, and gratitude, removes some widgets, and changes the mainMenuButton text
    if game["question_number"] == 11:
        feedbackLabel.config(text="Game Over!", background="gray")
        displayProblemButton.place_forget()
        submitButton.place_forget()
        displayScoreLabel.config(text=f"Total Score: {game['score']}")
        displayProblemLabel.config(text="Thanks for trying out my program!")
        mainMenuButton.config(text="Play Again or Exit")

# changes the background according to the parameter entered, from easy to hard difficulties
def change_background(diff):
    if diff == 1:
        playFrameBackground.config(image=easyDiffPhoto)
    elif diff == 2:
        playFrameBackground.config(image=medDiffPhoto)
    else:
        playFrameBackground.config(image=hardDiffPhoto)

# <--- Play Frame Widgets --->
    # This is the frame created when a player has chosen any from the 3 difficulties from the main menu
playFrameBackground = Label(playFrame)
playFrameBackground.place(x=0, y=0, relwidth=1, relheight=1) # Fills the entire window

    # This is the main menu button and if pressed runs two functions that switches to the main menu frame and resets the game stats
mainMenuButton = Button(playFrame, text="Main Menu", command=lambda: [switch_frame(mainMenuFrame), reset_game()])
mainMenuButton.place(x=400, y=500, anchor=CENTER) # Places the button somewhere in bottom middle area

    # This is the feedback label used to display feedback to the user 
    # Gives a welcome message and sets the background according to the play frame's background
feedbackLabel = Label(playFrame, text="Welcome to my Maths Quiz!", background=playFrame["background"])
feedbackLabel.place(x=400, y=225, anchor=CENTER) # Places the label somewhere in the middle top

    # This is the display problem label where the problem is displayed.
    # Also guides the user how to start the quiz
displayProblemLabel = Label(playFrame, text='Press "Display Problem" to start', background=playFrame["background"])
displayProblemLabel.place(x=400, y=250, anchor=CENTER) # Placed below the feedback label

    # This is the answer entry where the user will input the answer
answerEntry = Entry(playFrame)
answerEntry.place(x=400, y=300, anchor=CENTER) # Placed in the middle of the frame

    # This is the displayScoreLabel used for displaying the question number first and then the total score after game ends
displayScoreLabel = Label(playFrame, text="Question Number: 1", background=playFrame["background"])
displayScoreLabel.place(x=275, y=300, anchor=CENTER) # Placed at the left side of the entry frame

    # This is the submit button used to submit the answer and runs the command "is_correct" to check if the answer is correct
submitButton = Button(playFrame, text="Submit", command=is_correct)
submitButton.place(x=525, y=300, anchor=CENTER)

    # This is the display problem button used to display the problem by running the "display_problem()" function
displayProblemButton = Button(playFrame, text="Display Problem", command=display_problem)
displayProblemButton.place(x=400, y=350, anchor=CENTER)


# <--- Main Menu Frame Widgets --->
    # This is the background label used to put whatever background image photo is chosen
backGroundLabel = Label(mainMenuFrame, image=background_photo)
backGroundLabel.place(x=0, y=0, relwidth=1, relheight=1) # Configured to fill entire window space   

    # These are the three difficulty buttons used for switching to the play frame by running the "switch_frame()" function
    # Also runs the "setDiff()" and "change_background()" functions to set game difficulty and background
easyButton = Button(mainMenuFrame, text="Easy", command=lambda: [switch_frame(playFrame), set_diff(1), change_background(1)])
easyButton.place(x=400, y=270, anchor=CENTER)

mediumButton = Button(mainMenuFrame, text="Medium", command=lambda: [switch_frame(playFrame), set_diff(2), change_background(2)])
mediumButton.place(x=400, y=300, anchor=CENTER)

hardButton = Button(mainMenuFrame, text="Hard", command=lambda: [switch_frame(playFrame), set_diff(3), change_background(3)])
hardButton.place(x=400, y=330, anchor=CENTER)

quitButton = Button(mainMenuFrame, text="Quit", command=lambda: exit())
quitButton.place(x=400, y=360, anchor=CENTER)

# Switches to main menu frame on program run
switch_frame(mainMenuFrame)

# Runs the tkinter event loop to display the tkinter window
mainloop()