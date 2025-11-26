# Import tkinter for gui, and random for choosing jokes randomly
from tkinter import *
import random

# Put contents of "randomJokes" inside text dictionary
    # This is to separate the setups and the punchlines
jokesAndPunchlines = {}

# Store the current joke or setup here to be used by the puncline
current_joke = ""

# Open the "randomJokes.txt" and for every line, use the '?' to separate the setups from the punclines and then add the '?' again as it was removed
    # Store the separated setups and punchlines in the jokesAndPunchlines dictionary
with open(r"Assessment 1 - Skills Portfolio\Exercises\Ex02_TellAJoke\randomJokes.txt", "r") as file:
    for line in file:
        joke, punchline = line.split("?", 1)
        jokesAndPunchlines[joke.strip()+"?"] = punchline.strip()

# Create the main window using tkinter; set the window title, geometry, background color, etc
main = Tk()
main.title("Alexa Tell Me A Joke")
main.geometry("800x600")
main.resizable(0,0)
main.config(background="black")


# <--- Create the buttons for telling the setup, showing the punchline, next joke, and quit along with their respective configurations and function calls --->
tellAJokeButton = Button(main, text="Alexa, tell me a joke", font=("Arial", 14), background="pink", command=lambda:showJoke())
tellAJokeButton.place(x=300, y=300, anchor=CENTER)

showPunchLineButton = Button(main, text="Show punchline", font=("Arial", 14), background="green", command=lambda:showPunchline())

nextJokeButton = Button(main, text="Next Joke", font=("Arial", 14), background="yellow", command=lambda:showJoke())

quitButton = Button(main, text="Quit", font=("Arial", 14),background="Red", command=lambda:quit())
quitButton.place(x=340, y=500, anchor=CENTER)


# <--- Make labels for the setups and the punchlines each with their own configurations --->
jokeLabel = Label(main, text="Joke goes here", font=("Arial", 20))

punchlineLabel = Label(main, text="", font=("Arial", 24), background="lightgreen")

# <--- Functions --->

def showJoke():
    # uses the global current_joke variable and places the randomly picked key from the jokesAndPunchlines dictionary using the random method inside it.
    global current_joke
    current_joke = random.choice(list(jokesAndPunchlines.keys()))
    jokeLabel.config(text=current_joke) # Display the current joke/setup in the jokeLabel

    # Hides some unnecessary labels and buttons every time the function is called.
        # To clean the window and declutter it.
    punchlineLabel.place_forget()
    showPunchLineButton.place_forget()
    tellAJokeButton.place_forget()
    nextJokeButton.place_forget()

    # Show the punchline button and place the joke label for them to appear on screen every time this function is called
    showPunchLineButton.place(x=460, y=500, anchor=CENTER)
    jokeLabel.place(x=400, y=250, anchor=CENTER)

def showPunchline():
    # Uses the global current joke variable and creates the punchline variable to retrieve the respective punchline from the current joke which is the key
    global current_joke
    punchline = jokesAndPunchlines[current_joke] # Displays the appropriate punchline depending on the key/current joke
    punchlineLabel.config(text=punchline) # Display punchline using punchlineLabel

    # Show the punchline label and the next joke button every time this function is called
    punchlineLabel.place(x=400, y=300, anchor=CENTER)
    nextJokeButton.place(x=460, y=500, anchor=CENTER)

    # Hide the punchline button every time this function is called; since it is unnecessary
    showPunchLineButton.place_forget()

# run tkinter window
mainloop()