from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter import scrolledtext

# -------------------------------
# Config / File path
# -------------------------------
main = Tk()
main.title("Student Manager")
main.geometry("1920x1080")
main.config(background="lightblue")

filePath = r"Assessment 1 - Skills Portfolio\Exercises\Ex03_StudentManager\studentMarks.txt"

students = []  # list of dicts

# -------------------------------
# Helper functions (calc, save, load)
# -------------------------------
def recalc_student(s):
    """Recalculate derived fields for a student dict (total, coursework_total, percentage, grade)."""
    s['coursework_total'] = sum(s.get('cw_marks', [0,0,0]))
    s['total'] = s['coursework_total'] + int(s.get('exam_mark', 0))
    s['percentage'] = (s['total'] / 160) * 100 if 160 else 0
    p = s['percentage']
    if p >= 70:
        s['grade'] = 'A'
    elif p >= 60:
        s['grade'] = 'B'
    elif p >= 50:
        s['grade'] = 'C'
    elif p >= 40:
        s['grade'] = 'D'
    else:
        s['grade'] = 'F'

def load_students():
    """Load from filePath into students list. Expects first line to be count."""
    global students
    students = []
    try:
        with open(filePath, "r") as f:
            lines = [line.rstrip("\n") for line in f if line.strip() != ""]
        if not lines:
            return
        # If first line is a count, skip it
        first = lines[0].strip()
        start = 1 if first.isdigit() else 0
        for line in lines[start:]:
            parts = [p.strip() for p in line.split(",")]
            if len(parts) == 6:
                snum = parts[0]
                name = parts[1]
                try:
                    cw_marks = [int(parts[2]), int(parts[3]), int(parts[4])]
                except ValueError:
                    # If parsing fails, skip this record
                    continue
                try:
                    exam = int(parts[5])
                except ValueError:
                    exam = 0
                s = {
                    "student_number": snum,
                    "name": name,
                    "cw_marks": cw_marks,
                    "exam_mark": exam
                }
                recalc_student(s)
                students.append(s)
    except FileNotFoundError:
        # If file doesn't exist, start with empty list
        students = []

def save_students():
    """Write students list back to file, with first line = count."""
    try:
        with open(filePath, "w") as f:
            f.write(f"{len(students)}\n")
            for s in students:
                # Write cw1,cw2,cw3 individually so file keeps same format
                cw1, cw2, cw3 = s.get('cw_marks', [0,0,0])
                f.write(f"{s['student_number']},{s['name']},{cw1},{cw2},{cw3},{s['exam_mark']}\n")
    except Exception as e:
        messagebox.showerror("Save Error", f"Failed to save file: {e}")

# -------------------------------
# UI: ScrolledText and header formatting
# -------------------------------
textArea = scrolledtext.ScrolledText(main, wrap=WORD, font=("Courier", 14))
textArea.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.85)

def write_header():
    header = f"{'Student No':12} {'Name':30} {'Coursework':12} {'Exam':8} {'Total':8} {'%':7} {'Grade':6}\n"
    header += "-" * 95 + "\n"
    return header

def display_students(list_to_display=None):
    """Display a list of students in the textArea (if None, display full students list)."""
    if list_to_display is None:
        list_to_display = students
    textArea.configure(state="normal")
    textArea.delete('1.0', END)
    textArea.insert(END, write_header())
    for s in list_to_display:
        row = f"{s['student_number']:<12} {s['name']:<30} {s['coursework_total']:<12} "
        row += f"{s['exam_mark']:<8} {s['total']:<8} {s['percentage']:<7.2f} {s['grade']:<6}\n"
        textArea.insert(END, row)
    # summary
    if list_to_display:
        num_students = len(list_to_display)
        avg_percentage = sum(s["percentage"] for s in list_to_display) / num_students if num_students > 0 else 0
        textArea.insert(END, "\nClass Summary:\n")
        textArea.insert(END, f"Number of Students: {num_students}\n")
        textArea.insert(END, f"Average Percentage: {avg_percentage:.2f}%\n")
    textArea.configure(state="disabled")

# -------------------------------
# Feature Implementations
# -------------------------------
def viewAll():
    display_students()

def viewIndividual():
    search = simpledialog.askstring("Search Student", "Enter student number or name (partial OK):")
    if not search:
        return
    search_low = search.lower()
    found = None
    for s in students:
        if search_low == s['student_number'].lower() or search_low in s['name'].lower():
            found = s
            break
    if found:
        display_students([found])
    else:
        messagebox.showinfo("Not found", "No matching student found.")

def showHighest():
    if not students:
        messagebox.showinfo("No Data", "No students available.")
        return
    highest = max(students, key=lambda x: x["percentage"])
    display_students([highest])

def showLowest():
    if not students:
        messagebox.showinfo("No Data", "No students available.")
        return
    lowest = min(students, key=lambda x: x["percentage"])
    display_students([lowest])

# --- 5. Sort student records (popup asks field and order) ---
def sortRecords():
    if not students:
        messagebox.showinfo("No Data", "No students available.")
        return

    # ask for field
    fields = {
        "1": ("student_number", "Student Number"),
        "2": ("name", "Name"),
        "3": ("coursework_total", "Coursework Total"),
        "4": ("exam_mark", "Exam Mark"),
        "5": ("total", "Total"),
        "6": ("percentage", "Percentage"),
        "7": ("grade", "Grade")
    }
    prompt = "Sort by (enter number):\n"
    for k, v in fields.items():
        prompt += f"{k}. {v[1]}\n"
    choice = simpledialog.askstring("Sort - Field", prompt)
    if not choice or choice not in fields:
        return
    field_key = fields[choice][0]

    order = simpledialog.askstring("Sort - Order", "Enter order: 'asc' or 'desc'").strip().lower() if simpledialog.askstring else ''
    if not order or order not in ('asc', 'desc'):
        return

    reverse = (order == 'desc')
    # sort with stable method; for grade and name use string lower
    if field_key == 'name' or field_key == 'grade' or field_key == 'student_number':
        students.sort(key=lambda x: str(x[field_key]).lower(), reverse=reverse)
    else:
        students.sort(key=lambda x: x.get(field_key, 0), reverse=reverse)
    display_students()

# --- 6. Add a student record ---
def addStudent():
    # Gather inputs
    snum = simpledialog.askstring("Add Student", "Enter student number (unique):")
    if not snum:
        return
    # check unique
    if any(s['student_number'] == snum for s in students):
        messagebox.showerror("Duplicate", "A student with that student number already exists.")
        return
    name = simpledialog.askstring("Add Student", "Enter student name:")
    if not name:
        return
    try:
        cw1 = int(simpledialog.askstring("Add Student", "Enter coursework 1 mark (int):"))
        cw2 = int(simpledialog.askstring("Add Student", "Enter coursework 2 mark (int):"))
        cw3 = int(simpledialog.askstring("Add Student", "Enter coursework 3 mark (int):"))
        exam = int(simpledialog.askstring("Add Student", "Enter exam mark (int):"))
    except (TypeError, ValueError):
        messagebox.showerror("Invalid Input", "Marks must be integers. Operation cancelled.")
        return

    new_s = {
        "student_number": snum,
        "name": name,
        "cw_marks": [cw1, cw2, cw3],
        "exam_mark": exam
    }
    recalc_student(new_s)
    students.append(new_s)
    save_students()
    messagebox.showinfo("Added", f"Student {name} added.")
    display_students()

# --- 7. Delete a student record ---
def deleteStudent():
    search = simpledialog.askstring("Delete Student", "Enter student number or exact name to delete:")
    if not search:
        return
    # find exact student_number match first, otherwise exact name
    to_delete = None
    for s in students:
        if search == s['student_number'] or search.lower() == s['name'].lower():
            to_delete = s
            break
    if not to_delete:
        messagebox.showinfo("Not found", "Student not found (exact number or name required).")
        return
    confirm = messagebox.askyesno("Confirm Delete", f"Delete {to_delete['name']} ({to_delete['student_number']})?")
    if not confirm:
        return
    students.remove(to_delete)
    save_students()
    messagebox.showinfo("Deleted", "Student removed.")
    display_students()

# --- 8. Update a student's record ---
def updateStudent():
    search = simpledialog.askstring("Update Student", "Enter student number or name (partial OK):")
    if not search:
        return
    search_low = search.lower()
    found = None
    for s in students:
        if search_low == s['student_number'].lower() or search_low in s['name'].lower():
            found = s
            break
    if not found:
        messagebox.showinfo("Not found", "No matching student found.")
        return

    # Choose which field(s) to update
    fields_prompt = ("Choose field to update (enter number):\n"
                     "1. Name\n"
                     "2. Coursework marks (all three)\n"
                     "3. Exam mark\n"
                     "4. Student number\n"
                     "5. Cancel\n")
    choice = simpledialog.askstring("Update Field", fields_prompt)
    if not choice:
        return

    if choice == '1':
        new_name = simpledialog.askstring("Update Name", "Enter new name:")
        if new_name:
            found['name'] = new_name
    elif choice == '2':
        try:
            cw1 = int(simpledialog.askstring("Update Coursework", "Enter coursework 1 mark:"))
            cw2 = int(simpledialog.askstring("Update Coursework", "Enter coursework 2 mark:"))
            cw3 = int(simpledialog.askstring("Update Coursework", "Enter coursework 3 mark:"))
            found['cw_marks'] = [cw1, cw2, cw3]
        except (TypeError, ValueError):
            messagebox.showerror("Invalid Input", "Marks must be integers. Update cancelled.")
            return
    elif choice == '3':
        try:
            exam = int(simpledialog.askstring("Update Exam", "Enter new exam mark:"))
            found['exam_mark'] = exam
        except (TypeError, ValueError):
            messagebox.showerror("Invalid Input", "Exam must be an integer. Update cancelled.")
            return
    elif choice == '4':
        new_num = simpledialog.askstring("Update Student Number", "Enter new student number:")
        if new_num:
            if any(s['student_number'] == new_num and s is not found for s in students):
                messagebox.showerror("Duplicate", "Another student already uses that number.")
                return
            found['student_number'] = new_num
    else:
        return

    # Recalc and save
    recalc_student(found)
    save_students()
    messagebox.showinfo("Updated", "Student record updated.")
    display_students()

# -------------------------------
# Buttons area
# -------------------------------
button_frame = Frame(main, bg="lightblue")
button_frame.place(relx=0.01, rely=0.87, relwidth=0.98, relheight=0.12)

Button(button_frame, text="View All Students", font=("Arial", 14), command=viewAll).pack(side=LEFT, padx=6)
Button(button_frame, text="View Individual", font=("Arial", 14), command=viewIndividual).pack(side=LEFT, padx=6)
Button(button_frame, text="Highest Scorer", font=("Arial", 14), command=showHighest).pack(side=LEFT, padx=6)
Button(button_frame, text="Lowest Scorer", font=("Arial", 14), command=showLowest).pack(side=LEFT, padx=6)
Button(button_frame, text="Sort Records", font=("Arial", 14), command=sortRecords).pack(side=LEFT, padx=6)
Button(button_frame, text="Add Student", font=("Arial", 14), command=addStudent).pack(side=LEFT, padx=6)
Button(button_frame, text="Delete Student", font=("Arial", 14), command=deleteStudent).pack(side=LEFT, padx=6)
Button(button_frame, text="Update Student", font=("Arial", 14), command=updateStudent).pack(side=LEFT, padx=6)
Button(button_frame, text="Quit", font=("Arial", 14), command=main.quit).pack(side=LEFT, padx=6)

# -------------------------------
# Initial load & display
# -------------------------------
load_students()
display_students()

main.mainloop()
