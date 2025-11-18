from tkinter import *
import json
import random

text = {}

# Convert text file → json dictionary
with open(r"Assessment 1 - Skills Portfolio\Exercises\Ex02_TellAJoke\randomJokes.txt", "r") as file:
    for line in file:
        joke, punchline = line.split("?", 1)
        text[joke.strip()+"?"] = punchline.strip()   # keep the "?" in joke

with open(r"Assessment 1 - Skills Portfolio\Exercises\Ex02_TellAJoke\randomJokes.json", "w") as file:
    json.dump(text, file, indent=1)

with open(r"Assessment 1 - Skills Portfolio\Exercises\Ex02_TellAJoke\randomJokes.json", "r") as file:
    data = json.load(file)

# Store the current random joke
current_joke = None


def showJoke():
    global current_joke
    current_joke = random.choice(list(data.keys()))
    jokeLabel.config(text=current_joke)
    punchlineLabel.config(text="")      # clear punchline


def showPunchline():
    if current_joke:
        punchlineLabel.config(text=data[current_joke])
    else:
        punchlineLabel.config(text="Press 'Tell me a joke' first!")


main = Tk()
main.title("Alexa Tell Me A Joke")
main.geometry("800x600")
main.resizable(0,0)
main.config(background="black")

tellAJokeButton = Button(main, text="Alexa, tell me a joke", font=("Arial", 12),
                         background="pink", command=showJoke)
tellAJokeButton.place(x=300, y=300, anchor=CENTER)

showPunchLineButton = Button(main, text="Show punchline", font=("Arial", 12),
                             background="lightgreen", command=showPunchline)
showPunchLineButton.place(x=500, y=300, anchor=CENTER)

nextJokeButton = Button(main, text="Next Joke", font=("Arial", 14),
                        background="yellow", command=showJoke)
nextJokeButton.place(x=400, y=450, anchor=CENTER)

quitButton = Button(main, text="Quit", font=("Arial", 14),
                    background="red", command=quit)
quitButton.place(x=400, y=500, anchor=CENTER)

jokeLabel = Label(main, text="Joke goes here", font=("Arial", 20), bg="black", fg="white")
jokeLabel.place(x=400, y=350, anchor=CENTER)

punchlineLabel = Label(main, text="", font=("Arial", 20), bg="black", fg="white")
punchlineLabel.place(x=400, y=400, anchor=CENTER)

mainloop()
