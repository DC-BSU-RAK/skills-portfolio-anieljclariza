from tkinter import *
from tkinter import scrolledtext

# -------------------------------
# Main window setup
# -------------------------------
main = Tk()
main.title("Student Manager")
main.geometry("1000x800")
main.resizable(0,0)
main.config(background="lightblue")

filePath = r"Assessment 1 - Skills Portfolio\Exercises\Ex03_StudentManager\studentMarks.txt"

students = []

# -------------------------------
# Read student data
# -------------------------------
with open(filePath, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 6:
            studentNumber = parts[0].strip()
            name = parts[1].strip()
            coursework_total = sum(int(parts[i]) for i in range(2,5))  # sum of 3 coursework marks
            exam_mark = int(parts[5].strip())
            total = coursework_total + exam_mark
            percentage = (total / 160) * 100

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
                "student_number": studentNumber,
                "name": name,
                "coursework_total": coursework_total,
                "exam_mark": exam_mark,
                "total": total,
                "percentage": percentage,
                "grade": grade
            })

# -------------------------------
# ScrolledText widget
# -------------------------------
textArea = scrolledtext.ScrolledText(main, wrap=WORD, font=("Courier", 14))
textArea.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.85)

# -------------------------------
# Column settings for alignment
# -------------------------------
header_fields = ['Student No', 'Name', 'Coursework', 'Exam', 'Total', '%', 'Grade']
column_widths = [12, 20, 12, 8, 8, 7, 6]  # width for each column

# -------------------------------
# Functions
# -------------------------------
def viewAll():
    textArea.configure(state="normal")
    textArea.delete('1.0', END)

    # Build header
    header = ""
    for field, width in zip(header_fields, column_widths):
        header += f"{field:<{width}} "
    header += "\n" + "-"*80 + "\n"
    textArea.insert(END, header)

    # Build rows
    for s in students:
        row = f"{s['student_number']:<12} {s['name']:<20} {s['coursework_total']:<12} {s['exam_mark']:<8} "
        row += f"{s['total']:<8} {s['percentage']:<7.2f} {s['grade']:<6}\n"
        textArea.insert(END, row)

    # Class summary
    num_students = len(students)
    avg_percentage = sum(s["percentage"] for s in students) / num_students if num_students > 0 else 0
    textArea.insert(END, "\nClass Summary:\n")
    textArea.insert(END, f"Number of Students: {num_students}\n")
    textArea.insert(END, f"Average Percentage: {avg_percentage:.2f}%\n")

    textArea.configure(state="disabled")

# -------------------------------
# Buttons
# -------------------------------
button_frame = Frame(main, bg="lightblue")
button_frame.place(relx=0.01, rely=0.87, relwidth=0.98, relheight=0.12)

viewAllButton = Button(button_frame, text="View All Students", font=("Arial", 16), command=viewAll)
viewAllButton.pack(side=LEFT, padx=10, pady=10)

quitButton = Button(button_frame, text="Quit", font=("Arial", 16), command=main.quit)
quitButton.pack(side=LEFT, padx=10, pady=10)

# -------------------------------
# Start main loop
# -------------------------------
main.mainloop()
