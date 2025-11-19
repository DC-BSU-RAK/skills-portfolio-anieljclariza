from tkinter import *
import json
import random

text = {}
current_joke = ""

with open(r"Assessment 1 - Skills Portfolio\Exercises\Ex02_TellAJoke\randomJokes.txt", "r") as file:
    for line in file:
        joke, punchline = line.split("?", 1)
        text[joke.strip()+"?"] = punchline.strip()

with open(r"Assessment 1 - Skills Portfolio\Exercises\Ex02_TellAJoke\randomJokes.json", "w") as file:
    json.dump(text, file, indent=1)

with open(r"Assessment 1 - Skills Portfolio\Exercises\Ex02_TellAJoke\randomJokes.json", "r") as file:
    data = json.load(file)

main = Tk()
main.title("Alexa Tell Me A Joke")
main.geometry("800x600")
main.resizable(0,0)
main.config(background="black")

tellAJokeButton = Button(main, text="Alexa, tell me a joke", font=("Arial", 14), background="pink", command=lambda:showJoke())
tellAJokeButton.place(x=300, y=300, anchor=CENTER)

showPunchLineButton = Button(main, text="Show punchline", font=("Arial", 14), background="green", command=lambda:showPunchline())

nextJokeButton = Button(main, text="Next Joke", font=("Arial", 14), background="yellow", command=lambda:showJoke())

quitButton = Button(main, text="Quit", font=("Arial", 14),background="Red", command=lambda:quit())
quitButton.place(x=340, y=500, anchor=CENTER)

jokeLabel = Label(main, text="Joke goes here", font=("Arial", 20))

punchlineLabel = Label(main, text="", font=("Arial", 24), background="lightgreen")

def showJoke():
    global current_joke
    current_joke = random.choice(list(data.keys()))
    jokeLabel.config(text=current_joke)
    punchlineLabel.place_forget()
    showPunchLineButton.place_forget()
    tellAJokeButton.place_forget()
    nextJokeButton.place_forget()
    showPunchLineButton.place(x=460, y=500, anchor=CENTER)
    jokeLabel.place(x=400, y=250, anchor=CENTER)

def showPunchline():
    global current_joke
    punchline = data[current_joke]
    punchlineLabel.config(text=punchline)
    punchlineLabel.place(x=400, y=300, anchor=CENTER)
    nextJokeButton.place(x=460, y=500, anchor=CENTER)
    showPunchLineButton.place_forget()

mainloop()