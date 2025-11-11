from tkinter import *
import random

# --- Global Variables ---
score = 0
current_question = 0
attempt = 1
difficulty = 1
num1, num2 = 0, 0
operator = '+'

# --- Functions ---

def displayMenu():
    """Display difficulty menu"""
    for widget in main.winfo_children():
        widget.destroy()
    Label(main, text="DIFFICULTY LEVEL", font=("Arial", 20)).pack(pady=50)
    Button(main, text="1. Easy", font=("Arial", 16), width=15, command=lambda: startQuiz(1)).pack(pady=10)
    Button(main, text="2. Moderate", font=("Arial", 16), width=15, command=lambda: startQuiz(2)).pack(pady=10)
    Button(main, text="3. Advanced", font=("Arial", 16), width=15, command=lambda: startQuiz(3)).pack(pady=10)

def randomInt():
    """Return random integer based on difficulty"""
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation():
    """Return '+' or '-' randomly"""
    return random.choice(['+', '-'])

def startQuiz(selected_difficulty):
    global difficulty, score, current_question
    difficulty = selected_difficulty
    score = 0
    current_question = 0
    nextQuestion()

def displayProblem():
    """Generate and display a new problem"""
    global num1, num2, operator, attempt
    num1 = randomInt()
    num2 = randomInt()
    operator = decideOperation()
    attempt = 1
    question_label.config(text=f"Q{current_question+1}: {num1} {operator} {num2} =")
    answer_entry.delete(0, END)
    feedback_label.config(text="")

def isCorrect():
    """Check the user's answer"""
    global score, attempt, current_question
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        feedback_label.config(text="⚠️ Enter a valid number")
        return
    
    correct_answer = num1 + num2 if operator == '+' else num1 - num2
    
    if user_answer == correct_answer:
        points = 10 if attempt == 1 else 5
        score += points
        feedback_label.config(text=f"✅ Correct! (+{points} points)")
        main.after(1000, nextQuestion)
    else:
        if attempt == 1:
            attempt += 1
            feedback_label.config(text="❌ Wrong! Try once more.")
        else:
            feedback_label.config(text=f"❌ Wrong again! The answer was {correct_answer}.")
            main.after(1000, nextQuestion)

def nextQuestion():
    """Move to the next question or show results"""
    global current_question
    current_question += 1
    if current_question > 10:
        displayResults()
    else:
        displayProblem()

def displayResults():
    """Show final score and grade"""
    for widget in main.winfo_children():
        widget.destroy()
    Label(main, text=f"Your Score: {score}/100", font=("Arial", 20)).pack(pady=50)
    
    # Determine grade
    if score > 90:
        grade = "A+"
    elif score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"
    else:
        grade = "D"
    
    Label(main, text=f"Grade: {grade}", font=("Arial", 18)).pack(pady=20)
    Button(main, text="Play Again", font=("Arial", 16), command=displayMenu).pack(pady=20)
    Button(main, text="Exit", font=("Arial", 16), command=main.destroy).pack(pady=10)

# --- GUI Setup ---
main = Tk()
main.title("Maths Quiz")
main.geometry("800x600")
main.configure(bg="gray")

question_label = Label(main, text="", font=("Arial", 24), bg="gray")
question_label.pack(pady=50)

answer_entry = Entry(main, font=("Arial", 20), justify='center')
answer_entry.pack(pady=10)

submit_btn = Button(main, text="Submit", font=("Arial", 16), command=isCorrect)
submit_btn.pack(pady=10)

feedback_label = Label(main, text="", font=("Arial", 16), bg="gray")
feedback_label.pack(pady=20)

displayMenu()
main.mainloop()