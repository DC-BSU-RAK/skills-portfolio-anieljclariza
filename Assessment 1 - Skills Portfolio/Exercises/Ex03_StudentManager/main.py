import tkinter as tk # for gui
from tkinter import simpledialog, messagebox # for query and text box

# Create main window using tkinter
    # Configure main window
main = tk.Tk()
main.title("Student Manager")
main.geometry("1366x768")
main.resizable(0,0)
main.config(background="lightblue")

# file path of "studentMarks.txt"
FILE_PATH = r"Assessment 1 - Skills Portfolio\Exercises\Ex03_StudentManager\studentMarks.txt"

# This function loads all the data from "studentMarks.txt" to be used by the program and also adds other student data such as grade, coursework total, total, and percentage
def loadStudents(filePath=FILE_PATH):
    students = [] # Create empty dictionary
    
    # Open the text file as "read-only" to access contents
    with open(filePath, "r") as file:
        class_count = int(file.readline().strip())
        
        # Separate each value in every line in the text file by comma
        for _ in range(class_count):
            line = file.readline().strip()
            
            # put line values in respective variable
            student_number, name, course_mark1, course_mark2, course_mark3, exam_mark = line.split(",")

            # convert marks to int
            course_mark1, course_mark2, course_mark3, exam_mark = map(int, (course_mark1, course_mark2, course_mark3, exam_mark))

            # add marks in total
            coursework_total = course_mark1 + course_mark2 + course_mark3
            overall_total = coursework_total + exam_mark

            # determine percentage based on total over total attainable
            percentage = (overall_total / 160) * 100

            # determine grade based on percentage
            if percentage >= 70: grade = 'A'
            elif percentage >= 60: grade = 'B'
            elif percentage >= 50: grade = 'C'
            elif percentage >= 40: grade = 'D'
            else: grade = 'F'

            # add student record values
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

# put student values in students dict
students = loadStudents()

# save data into "studentMarks.txt"
def saveStudents():
    with open(FILE_PATH, "w") as file:
        file.write(f"{len(students)}\n")
        for s in students:
            line = f"{s['student_number']},{s['name']},{s['course_mark1']},{s['course_mark2']},{s['course_mark3']},{s['exam_mark']}\n"
            file.write(line)

# this just formats the text box display for better readability
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

# this outputs text in textbox
def showOutput(text):
    text_box.config(state="normal")
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, text)
    text_box.config(state="disabled")

# -this shows all student records
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

# view individual student record based on user input
def viewIndividual():
    # ask query for student name or student number
    query = simpledialog.askstring("Search Student", "Enter student name/student number:")

    if not query:
        return
    
    # make query lowercase for later 
    query = query.lower()

    # output student record based on student
    for s in students:
        if query in s["name"].lower() or query == s["student_number"]:
            showOutput(formatStudent(s))
            return
    messagebox.showinfo("Not Found", "Student not found.")

# Show highest scorer using max() method with other code
def showHighest():
    if not students: return

    # Use max() method to find highest scorer in students dictionary and output properly
    highest = max(students, key=lambda x: x["percentage"])
    showOutput("Highest Scoring Student:\n\n" + formatStudent(highest))

# Show lowest scorer using min() method with other code in students dictionary
def showLowest():
    if not students: return
    lowest = min(students, key=lambda x: x["percentage"])
    showOutput("Lowest Scoring Student:\n\n" + formatStudent(lowest))

# this sorts the student record based on user choice
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

    # sorting options
    field_map = {
        1: "name",
        2: "student_number",
        3: "percentage",
        4: "grade",
        5: "coursework_total",
        6: "exam_mark"
    }

    # error checking
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

# this adds a student based on given details on the text file
def addStudent():
    # asks for student number of new student
    student_number = simpledialog.askstring("Add Student", "Enter Student Number:")
    if not student_number: return

    # asks for name of new student
    name = simpledialog.askstring("Add Student", "Enter Student Name:")
    if not name: return

    # asks for marks of new student
    try:
        course_mark1 = int(simpledialog.askstring("Add Student", "Enter Coursework Mark 1 (0-40):"))
        course_mark2 = int(simpledialog.askstring("Add Student", "Enter Coursework Mark 2 (0-40):"))
        course_mark3 = int(simpledialog.askstring("Add Student", "Enter Coursework Mark 3 (0-40):"))
        exam_mark = int(simpledialog.askstring("Add Student", "Enter Exam Mark (0-40):"))

    # catch any errors
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Input", "Marks must be integer values.")
        return
    
    # calculate scores
    coursework_total = course_mark1 + course_mark2 + course_mark3
    overall_total = coursework_total + exam_mark
    percentage = (overall_total / 160) * 100

    # determine grade
    if percentage >= 70: grade = 'A'
    elif percentage >= 60: grade = 'B'
    elif percentage >= 50: grade = 'C'
    elif percentage >= 40: grade = 'D'
    else: grade = 'F'

    # add values of new student 
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
    # save student
    saveStudents()
    messagebox.showinfo("Success", f"Student {name} added successfully.")

    # show all student records to verify changes
    viewAll()

# this deletes the student 
def deleteStudent():
    # asks for student name or number
    query = simpledialog.askstring("Delete Student", "Enter student name/student number:")

    if not query: return

    query = query.lower() # make query lowercase for later

    # deletes student and saves changes in text file
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

# changes student values
def updateStudent():
    # asks user for student name or number and stores in "query"
    query = simpledialog.askstring("Update Student", "Enter student name/student number:")

    if not query: return
    
    query = query.lower() # make query lowercase for later

    # run for loop finding student and changing respective options
    for s in students:
        if query in s["name"].lower() or query == s["student_number"]:
            # Show sub-menu for which field to update
            choice = simpledialog.askinteger(
                "Update Menu",
                "Choose field to update:\n1. Name\n2. Coursework Mark 1\n3. Coursework Mark 2\n4. Coursework Mark 3\n5. Exam Mark"
            )
            # changes values based on which field user has chosesn to change
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

            # update studentMarks.txt
            saveStudents()
            messagebox.showinfo("Updated", f"Student {s['name']} updated successfully.")

            # show all student records to verify changes
            viewAll()
            return
    messagebox.showinfo("Not Found", "Student not found.")

# text box creation and configuration
text_box = tk.Text(main, font=("Arial", 16))
text_box.pack(expand=True, fill="both", padx=10, pady=10)
text_box.config(state="disabled")

# frame to put buttons on
frame = tk.Frame(main)
frame.pack(pady=10)

# make a list containing button names and their function calls
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

# how many buttons per row
columns_per_row = 4

# place buttons in grid from buttons list above
for i, (text, command) in enumerate(buttons):
    row = i // columns_per_row
    col = i % columns_per_row
    tk.Button(frame, text=text, font=("Arial",16), width=25, command=command).grid(row=row, column=col, padx=5, pady=5)

main.mainloop() # start gui