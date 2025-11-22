from tkinter import *

main = Tk()
main.title("Student Manager")
main.geometry("1000x1000")
main.resizable(0,0)
main.config(background="black")

viewAll = Button(main, text="View All Student Records", font=("Arial", 20))
viewAll.place(x=500, y=350, anchor=CENTER)

viewIndividual = Button(main, text="View Individual Student Record", font=("Arial", 20))
viewIndividual.place(x=500, y=425, anchor=CENTER)

showHighest = Button(main, text="Show Highest Scorer", font=("Arial", 20))
showHighest.place(x=500, y=500, anchor=CENTER)

showLowest = Button(main, text="Show Lowest Scorer", font=("Arial",20))
showLowest.place(x=500, y=575, anchor=CENTER)

quitButton = Button(main, text="Quit", font=("Arial", 20), command=lambda: quit())
quitButton.place(x=500, y=650, anchor=CENTER)

mainloop()