import tkinter as tk # for gui
from tkinter import simpledialog, messagebox # for query and message display
import os # for file pathing

# Main window creation and configuration
main = tk.Tk()
main.title("Student Manager")
main.geometry("1366x768")
main.resizable(0,0)
main.config(background="lightblue")

# File path of student marks
FILE_PATH = r"Assessment 1 - Skills Portfolio\Exercises\Ex03_StudentManager\studentMarks.txt"

# --- Load Students ---
def loadStudents(filePath=FILE_PATH):
    students = []
    if not os.path.exists(filePath):
        return students
    
    with open(filePath, "r") as file:
        try:
            class_count = int(file.readline().strip())
        except ValueError:
            class_count = 0

        for _ in range(class_count):
            line = file.readline().strip()
            if not line:
                continue
            student_number, name, course_mark1, course_mark2, course_mark3, exam_mark = line.split(",")
            course_mark1, course_mark2, course_mark3, exam_mark = map(int, (course_mark1, course_mark2, course_mark3, exam_mark))
            coursework_total = course_mark1 + course_mark2 + course_mark3
            overall_total = coursework_total + exam_mark
            percentage = (overall_total / 160) * 100
            if percentage >= 70: grade = 'A'
            elif percentage >= 60: grade = 'B'
            elif percentage >= 50: grade = 'C'
            elif percentage >= 40: grade = 'D'
            else: grade = 'F'
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

# --- Save Students Back to File ---
def saveStudents():
    with open(FILE_PATH, "w") as file:
        file.write(f"{len(students)}\n")
        for s in students:
            line = f"{s['student_number']},{s['name']},{s['course_mark1']},{s['course_mark2']},{s['course_mark3']},{s['exam_mark']}\n"
            file.write(line)

# --- Format Student for Display ---
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

# --- Display Output in TextBox ---
def showOutput(text):
    text_box.config(state="normal")
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, text)
    text_box.config(state="disabled")

# --- View All Students ---
def viewAll():
    output = ""
    total_percent = 0
    for s in students:
        output += formatStudent(s)
        total_percent += s["percentage"]
    if students:
        avg_percentage = total_percent / len(students)
        output += f"\nTotal Students: {len(students)}\n"
        output += f"Class Average Percentage: {avg_percentage:.2f}%"
    showOutput(output)

# --- View Individual Student ---
def viewIndividual():
    query = simpledialog.askstring("Search Student", "Enter student name/student number:")
    if not query:
        return
    query = query.lower()
    for s in students:
        if query in s["name"].lower() or query == s["student_number"]:
            showOutput(formatStudent(s))
            return
    messagebox.showinfo("Not Found", "Student not found.")

# --- Show Highest and Lowest ---
def showHighest():
    if not students: return
    highest = max(students, key=lambda x: x["percentage"])
    showOutput("Highest Scoring Student:\n\n" + formatStudent(highest))

def showLowest():
    if not students: return
    lowest = min(students, key=lambda x: x["percentage"])
    showOutput("Lowest Scoring Student:\n\n" + formatStudent(lowest))

# --- Sort Students ---
# --- Expanded Sort Students ---
def sortStudents():
    if not students:
        messagebox.showinfo("No Data", "No students to sort.")
        return

    # Ask user which field to sort by
    field_choice = simpledialog.askinteger(
        "Sort Students",
        "Choose field to sort by:\n"
        "1. Name\n"
        "2. Student Number\n"
        "3. Percentage\n"
        "4. Grade\n"
        "5. Coursework Total\n"
        "6. Exam Mark"
    )
    if not field_choice:
        return

    field_map = {
        1: "name",
        2: "student_number",
        3: "percentage",
        4: "grade",
        5: "coursework_total",
        6: "exam_mark"
    }

    field = field_map.get(field_choice)
    if not field:
        messagebox.showerror("Invalid Input", "Invalid choice.")
        return

    # Ask user for sorting order
    order = simpledialog.askstring("Sort Order", "Enter 'asc' for ascending or 'desc' for descending:")
    if not order:
        return

    order = order.lower()
    reverse = False
    if order == "desc":
        reverse = True
    elif order != "asc":
        messagebox.showerror("Invalid Input", "Please enter 'asc' or 'desc'.")
        return

    # Sort the students list based on the chosen field
    try:
        sorted_list = sorted(students, key=lambda x: x[field], reverse=reverse)
    except KeyError:
        messagebox.showerror("Error", "Cannot sort by this field.")
        return

    # Display sorted students
    output = ""
    total_percent = 0
    for s in sorted_list:
        output += formatStudent(s)
        total_percent += s["percentage"]
    avg_percentage = total_percent / len(sorted_list)
    output += f"\nTotal Students: {len(sorted_list)}\n"
    output += f"Class Average Percentage: {avg_percentage:.2f}%"
    showOutput(output)

# --- Add Student ---
def addStudent():
    student_number = simpledialog.askstring("Add Student", "Enter Student Number:")
    if not student_number: return
    name = simpledialog.askstring("Add Student", "Enter Student Name:")
    if not name: return
    try:
        course_mark1 = int(simpledialog.askstring("Add Student", "Enter Coursework Mark 1 (0-40):"))
        course_mark2 = int(simpledialog.askstring("Add Student", "Enter Coursework Mark 2 (0-40):"))
        course_mark3 = int(simpledialog.askstring("Add Student", "Enter Coursework Mark 3 (0-40):"))
        exam_mark = int(simpledialog.askstring("Add Student", "Enter Exam Mark (0-40):"))
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Input", "Marks must be integer values.")
        return
    coursework_total = course_mark1 + course_mark2 + course_mark3
    overall_total = coursework_total + exam_mark
    percentage = (overall_total / 160) * 100
    if percentage >= 70: grade = 'A'
    elif percentage >= 60: grade = 'B'
    elif percentage >= 50: grade = 'C'
    elif percentage >= 40: grade = 'D'
    else: grade = 'F'
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
    saveStudents()
    messagebox.showinfo("Success", f"Student {name} added successfully.")
    viewAll()

# --- Delete Student ---
def deleteStudent():
    query = simpledialog.askstring("Delete Student", "Enter student name/student number:")
    if not query: return
    query = query.lower()
    for i, s in enumerate(students):
        if query in s["name"].lower() or query == s["student_number"]:
            confirm = messagebox.askyesno("Confirm Delete", f"Delete {s['name']}?")
            if confirm:
                students.pop(i)
                saveStudents()
                messagebox.showinfo("Deleted", f"Student {s['name']} deleted.")
                viewAll()
            return
    messagebox.showinfo("Not Found", "Student not found.")

# --- Update Student ---
def updateStudent():
    query = simpledialog.askstring("Update Student", "Enter student name/student number:")
    if not query: return
    query = query.lower()
    for s in students:
        if query in s["name"].lower() or query == s["student_number"]:
            # Show sub-menu for which field to update
            choice = simpledialog.askinteger(
                "Update Menu",
                "Choose field to update:\n1. Name\n2. Coursework Mark 1\n3. Coursework Mark 2\n4. Coursework Mark 3\n5. Exam Mark"
            )
            if choice == 1:
                new_name = simpledialog.askstring("Update", "Enter new name:")
                if new_name: s["name"] = new_name
            elif choice in [2,3,4,5]:
                try:
                    new_mark = int(simpledialog.askstring("Update", "Enter new mark (0-40):"))
                except (ValueError, TypeError):
                    messagebox.showerror("Invalid Input", "Mark must be integer.")
                    return
                if choice == 2: s["course_mark1"] = new_mark
                if choice == 3: s["course_mark2"] = new_mark
                if choice == 4: s["course_mark3"] = new_mark
                if choice == 5: s["exam_mark"] = new_mark
            else:
                return
            # Recalculate totals
            s["coursework_total"] = s["course_mark1"] + s["course_mark2"] + s["course_mark3"]
            overall_total = s["coursework_total"] + s["exam_mark"]
            s["percentage"] = (overall_total / 160) * 100
            if s["percentage"] >= 70: s["grade"] = 'A'
            elif s["percentage"] >= 60: s["grade"] = 'B'
            elif s["percentage"] >= 50: s["grade"] = 'C'
            elif s["percentage"] >= 40: s["grade"] = 'D'
            else: s["grade"] = 'F'
            saveStudents()
            messagebox.showinfo("Updated", f"Student {s['name']} updated successfully.")
            viewAll()
            return
    messagebox.showinfo("Not Found", "Student not found.")

# --- GUI Components ---
text_box = tk.Text(main, font=("Arial", 16))
text_box.pack(expand=True, fill="both", padx=10, pady=10)
text_box.config(state="disabled")

frame = tk.Frame(main)
frame.pack(pady=10)

# --- Buttons Configuration ---
buttons = [
    ("1. View All Students", viewAll),
    ("2. View Individual Student", viewIndividual),
    ("3. Show Highest Score", showHighest),
    ("4. Show Lowest Score", showLowest),
    ("5. Sort Record", sortStudents),
    ("6. Add Student", addStudent),
    ("7. Delete Student", deleteStudent),
    ("8. Update Student", updateStudent),
]

# How many buttons per row
columns_per_row = 4

# Place buttons in grid
for i, (text, command) in enumerate(buttons):
    row = i // columns_per_row
    col = i % columns_per_row
    tk.Button(frame, text=text, font=("Arial",16), width=25, command=command).grid(row=row, column=col, padx=5, pady=5)

# --- Start GUI ---
main.mainloop()