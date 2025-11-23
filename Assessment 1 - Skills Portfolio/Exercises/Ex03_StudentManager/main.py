import tkinter as tk # for gui
from tkinter import simpledialog, messagebox # for query and text box

# Create main window using tkinter
    # Configure main window
main = tk.Tk()
main.title("Student Manager")
main.geometry("1366x768")
main.resizable(0,0)
main.config(background="lightblue")

# This function loads all the data from "studentMarks.txt" to be used by the program and also adds other student data such as grade, coursework total, total, and percentage
def loadStudents(filePath = r"Assessment 1 - Skills Portfolio\Exercises\Ex03_StudentManager\studentMarks.txt"):
    students = [] # Create empty dictionary

    # Open the text file as "read-only" to access contents
    with open(filePath, "r") as file:
        class_count = int(file.readline().strip())

        # Separate each value in every line in the text file by comma
        for _ in range(class_count):
            line = file.readline().strip()
            if not line:
                continue
            student_number, name, course_mark1, course_mark2, course_mark3, exam_mark = line.split(",")

            # Make coursework marks of integer value to be used for arithmetics
            course_mark1, course_mark2, course_mark3, exam_mark = int(course_mark1), int(course_mark2), int(course_mark3), int(exam_mark)

            # Calculate required values such as coursework marks total, overall total, and percentage
            coursework_total = (course_mark1 + course_mark2 + course_mark3)
            overall_total = (coursework_total + exam_mark)
            percentage = (overall_total / 160) * 100 

            # Calculate student grade based on percentage
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

            # Add all student data inside the students dictionary
            students.append({
                "student_number": student_number,
                "name": name,
                "coursework_total": coursework_total,
                "exam_mark": exam_mark,
                "percentage": percentage,
                "grade": grade
            })
    
        # return students to be used outside of function
        return students

# Put all student data in students dictionary
students = loadStudents()

# This formats all student records and data to place them in textbox properly and cleanly
def formatStudent(s):
    return(
        f"Name: {s['name']}\n"
        
        f"Student Number: {s['student_number']}\n"

        f"Coursework Total Mark: {s['coursework_total']}\n"

        f"Exam Mark: {s['exam_mark']}\n"

        f"Overall %: {s['percentage']:.2f}\n"
        
        f"Grade: {s['grade']}\n"

        # This one just adds a long line of '-'s every student for cleanliness
        f"{'-'*40}\n"
    )

# This function just formats the incoming text before displaying it in text box, ensuring everything is outputted properly before and afterwards
def showOutput(text):
    text_box.config(state="normal") # Allow typing
    text_box.delete("1.0", tk.END) # Delete all previous contents of text box
    text_box.insert(tk.END, text) # Insert respective text
    text_box.config(state="disabled") # Disable textbox typing

# This displays all students' records and data in students dictionary
def viewAll():
    # Make intial variable to store data later on
    output = ""
    total_percent = 0

    # Make for loop and output every student record and also add total_percent
    for s in students:
        output += formatStudent(s)
        total_percent += s["percentage"]
    
    # Calculate average percentage based on total percentage divided by total students in class
    avg_percentage = total_percent / len(students)

    # Output results with some formatting
    output += f"\nTotal Students: {len(students)}\n"
    output += f"Class Average Percentage: {avg_percentage:.2f}%"

    # This outputs everything in output variable
    showOutput(output)

# View individual student records
def viewIndividual():
    # Asks for student name or student number using simpledialog.askstring and stores input in query variable
    query = simpledialog.askstring(
        "Searh Student",
        "Enter student name/student number: "
    )
    
    # Make query all lowercase for uniformity
    query = query.lower()

    # Make for loop and if query is found in students dictionary, use showOutput to output respective student data
    for s in students: 
        if query in s["name"].lower() or query == s["student_number"]:
            showOutput(formatStudent(s))
            return
    
# Show highest scorer using max() method with other code
def showHighest():
    if not students:
        return
    
    # Delete textbox contents before pasting the new info
    text_box.delete("1.0", tk.END)
    
    # Use max() method to find highest scorer in students dictionary and output properly
    highest = max(students, key=lambda x: x["percentage"])
    showOutput("Highest Scoring Student:\n\n" + formatStudent(highest))

# Show lowest scorer using min() method with other code in students dictionary
def showLowest():
    if not students:
        return

    # Use min() method to find lowest scorer
    lowest = min(students, key=lambda x: x["percentage"])

    # Delete textbox contents before pasting the new info
    text_box.delete("1.0", tk.END)

    # This shows the output and by calling the formatStudent on lowest
    showOutput("Lowest Scoring Student: \n\n" + formatStudent(lowest))

# Create text box to place the students' info later with its own configurations and to make sure it cannot be typed on for cleanliness
# Place it and make it fill entire main window with its own padding as well
text_box = tk.Text(main, font=("Arial", 16))
text_box.pack(expand=True, fill="both", padx=10, pady=10)
text_box.config(state="disabled")

# Make frame frame on main window and pack it to place the buttons in it
frame = tk.Frame(main)
frame.pack(pady=10)

# Create respective buttons with their respective configurations and function calls and place them in frame
viewAllButton = tk.Button(frame, text="1. View All Students", font=("Arial", 16), width=25, command=viewAll)
viewIndividualButton = tk.Button(frame, text="2. View Individual Student", width=25, font=("Arial", 16), command=viewIndividual)
viewHighestButton = tk.Button(frame, text="3. Show Highest Score", width=25, font=("Arial", 16),command=showHighest)
viewLowestButton = tk.Button(frame, text="4. Show Lowest Score", width=25, font=("Arial", 16),command=showLowest)

# Place respective buttons in their respective positions with their own paddings
viewAllButton.grid(row=0, column=0, padx=5, pady=5)
viewIndividualButton.grid(row=0, column=1, padx=5, pady=5)
viewHighestButton.grid(row=0, column=2, padx=5, pady=5)
viewLowestButton.grid(row=0, column=3, padx=5, pady=5)

# Start mainloop to show main window
main.mainloop()