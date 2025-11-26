import tkinter as tk
from tkinter import simpledialog, messagebox

main = tk.Tk()
main.title("Student Manager")
main.geometry("1366x768")
main.resizable(0,0)
main.config(background="lightblue")

def loadStudents(filePath = r"Assessment 1 - Skills Portfolio\Exercises\Ex03_StudentManager\studentMarks.txt"):
    students = []
    with open(filePath, "r") as file:
        class_count = int(file.readline().strip())
        for _ in range(class_count):
            line = file.readline().strip()
            
            # put line values in respective variable
            student_number, name, course_mark1, course_mark2, course_mark3, exam_mark = line.split(",")

            course_mark1, course_mark2, course_mark3, exam_mark = int(course_mark1), int(course_mark2), int(course_mark3), int(exam_mark)

            coursework_total = (course_mark1 + course_mark2 + course_mark3)
            overall_total = (coursework_total + exam_mark)
            percentage = (overall_total / 160) * 100

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
                "student_number": student_number,
                "name": name,
                "course_mark1": course_mark1,
                "course_mark2": course_mark2,
                "course_mark3": course_mark3,
                "exam_mark": exam_mark,
                "coursework_total": coursework_total,
                "percentage": percentage,
                "grade": grade
            })

        return students

students = loadStudents()

def formatStudent(s):
    return(
        f"Name: {s['name']}\n"
        f"Student Number: {s['student_number']}\n"
        f"Coursework Marks: {s['course_mark1']}, {s['course_mark2']}, {s['course_mark3']}\n"
        f"Coursework Total: {s['coursework_total']}\n"
        f"Exam Mark: {s['exam_mark']}\n"
        f"Overall %: {s['percentage']:.2f}\n"
        f"Grade: {s['grade']}\n"

        f"{'-'*40}\n"
    )

def showOutput(text):
    text_box.config(state="normal")
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, text)
    text_box.config(state="disabled")

def viewAll():
    output = ""
    total_percent = 0

    for s in students:
        output += formatStudent(s)
        total_percent += s["percentage"]
    
    avg_percentage = total_percent / len(students)
    output += f"\nTotal Students: {len(students)}\n"
    output += f"Class Average Percentage: {avg_percentage:.2f}%"

    showOutput(output)

def viewIndividual():
    query = simpledialog.askstring(
        "Searh Student",
        "Enter student name/student number: "
    )

    if not query:
        messagebox.showerror("Error", "Please input correct student data")
        return
    
    query = query.lower()
    for s in students: 
        if query in s["name"].lower() or query == s["student_number"]:
            showOutput(formatStudent(s))
            return
    

def showHighest():
    if not students:
        return
    highest = max(students, key=lambda x: x["percentage"])
    showOutput("Highest Scoring Student:\n\n" + formatStudent(highest))

def showLowest():
    if not students: return
    lowest = min(students, key=lambda x: x["percentage"])
    showOutput("Lowest Scoring Student:\n\n" + formatStudent(lowest))

# this sorts the student record based on user choice
def sortStudents():
    if not students:
        messagebox.showinfo("No Data", "No students to sort.")
        return
    lowest = min(students, key=lambda x: x["percentage"])
    text_box.delete("1.0", tk.END)
    showOutput("Lowest Scoring Student: \n\n" + formatStudent(lowest))

text_box = tk.Text(main, font=("Arial", 16))
text_box.pack(expand=True, fill="both", padx=10, pady=10)
text_box.config(state="disabled")

frame = tk.Frame(main)
frame.pack(pady=10)

btn1 = tk.Button(frame, text="1. View All Students", width=25, command=viewAll)
btn2 = tk.Button(frame, text="2. View Individual Student", width=25, command=viewIndividual)
btn3 = tk.Button(frame, text="3. Show Highest Score", width=25, command=showHighest)
btn4 = tk.Button(frame, text="4. Show Lowest Score", width=25, command=showLowest)

btn1.grid(row=0, column=0, padx=5, pady=5)
btn2.grid(row=1, column=0, padx=5, pady=5)
btn3.grid(row=2, column=0, padx=5, pady=5)
btn4.grid(row=3, column=0, padx=5, pady=5)

main.mainloop()
