from tkinter import *
from tkinter import scrolledtext

# File path
filePath = r"Assessment 1 - Skills Portfolio\Exercises\Ex03_StudentManager\studentMarks.txt"

# Read student data from file
students = []
with open(filePath, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 4:
            name = parts[0].strip()
            number = parts[1].strip()
            coursework = float(parts[2].strip())
            exam = float(parts[3].strip())
            total = coursework + exam
            percentage = (total / 160) * 100  # Total marks = 160

            # Determine grade
            if percentage >= 70:
                grade = 'A'
            elif percentage >= 60:
                grade = 'B'
            elif percentage >= 50:
                grade = 'C'
            elif percentage >= 40:
                grade = 'D'
            else:
                grade = 'F'

            students.append({
                "name": name,
                "number": number,
                "coursework": coursework,
                "exam": exam,
                "total": total,
                "percentage": percentage,
                "grade": grade
            })

# Create main window
main = Tk()
main.title("Student Manager")
main.geometry("1000x800")

# Scrolled text area with monospaced font for alignment
textArea = scrolledtext.ScrolledText(main, wrap=WORD, font=("Courier", 14))
textArea.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.95)

# Function to view all students in formatted table
def viewAll():
    textArea.configure(state="normal")
    textArea.delete('1.0', END)
    
    # Header
    header = f"{'Name':20} {'Student No':12} {'Coursework':10} {'Exam':6} {'Total':6} {'%':7} {'Grade':6}\n"
    textArea.insert(END, header)
    textArea.insert(END, "-"*75 + "\n")
    
    # Student data
    for s in students:
        line = f"{s['name']:20} {s['number']:12} {s['coursework']:10} {s['exam']:6} {s['total']:6} {s['percentage']:7.2f} {s['grade']:6}\n"
        textArea.insert(END, line)
    
    # Summary
    num_students = len(students)
    avg_percentage = sum(s["percentage"] for s in students) / num_students if num_students > 0 else 0
    textArea.insert(END, "\nClass Summary:\n")
    textArea.insert(END, f"Number of Students: {num_students}\n")
    textArea.insert(END, f"Average Percentage: {avg_percentage:.2f}%\n")
    
    textArea.configure(state="disabled")

# Button to view all students
viewAllBtn = Button(main, text="View All Student Records", font=("Arial", 20), command=viewAll)
viewAllBtn.place(x=500, y=750, anchor=CENTER)

main.mainloop()