import tkinter as tk
from tkinter import messagebox, simpledialog


# ----------------------------
# Load Student File
# ----------------------------

def load_students(filename=r"Assessment 1 - Skills Portfolio\Exercises\Ex03_StudentManager\studentMarks.txt"):
    students = []
    try:
        with open(filename, "r") as f:
            count = int(f.readline().strip())  # first line is number of students
            for _ in range(count):
                line = f.readline().strip()
                if not line:
                    continue
                code, name, c1, c2, c3, exam = line.split(",")

                c1, c2, c3, exam = int(c1), int(c2), int(c3), int(exam)
                cw_total = c1 + c2 + c3
                total = cw_total + exam  # out of 160
                percent = (total / 160) * 100

                # determine grade
                if percent >= 70:
                    grade = "A"
                elif percent >= 60:
                    grade = "B"
                elif percent >= 50:
                    grade = "C"
                elif percent >= 40:
                    grade = "D"
                else:
                    grade = "F"

                students.append({
                    "code": code,
                    "name": name,
                    "cw_total": cw_total,
                    "exam": exam,
                    "percent": percent,
                    "grade": grade
                })

    except FileNotFoundError:
        messagebox.showerror("Error", "studentMarks.txt not found.")
    return students


students = load_students()


# ----------------------------
# Helper: Format Student Info
# ----------------------------

def format_student(s):
    return (
        f"Name: {s['name']}\n"
        f"Student Number: {s['code']}\n"
        f"Coursework Total: {s['cw_total']}\n"
        f"Exam Mark: {s['exam']}\n"
        f"Overall %: {s['percent']:.2f}%\n"
        f"Grade: {s['grade']}\n"
        f"{'-'*40}\n"
    )


# ----------------------------
# Menu Functions
# ----------------------------

def view_all():
    if not students:
        messagebox.showerror("Error", "No student data loaded.")
        return

    output = ""
    total_percent = 0

    for s in students:
        output += format_student(s)
        total_percent += s["percent"]

    avg_percent = total_percent / len(students)
    output += f"\nTotal Students: {len(students)}\n"
    output += f"Average Percentage: {avg_percent:.2f}%"

    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, output)


def view_individual():
    if not students:
        messagebox.showerror("Error", "No student data loaded.")
        return

    query = simpledialog.askstring(
        "Search Student",
        "Enter student name or student number:"
    )

    if not query:
        return

    query = query.lower()
    for s in students:
        if query in s["name"].lower() or query == s["code"]:
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, format_student(s))
            return

    messagebox.showinfo("Not Found", "No matching student found.")


def show_highest():
    if not students:
        return
    best = max(students, key=lambda x: x["percent"])
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, "Highest Scoring Student:\n\n")
    text_box.insert(tk.END, format_student(best))


def show_lowest():
    if not students:
        return
    worst = min(students, key=lambda x: x["percent"])
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, "Lowest Scoring Student:\n\n")
    text_box.insert(tk.END, format_student(worst))


# ----------------------------
# Tkinter GUI Setup
# ----------------------------

root = tk.Tk()
root.title("Student Marks Manager")
root.geometry("650x500")

frame = tk.Frame(root)
frame.pack(pady=10)

btn1 = tk.Button(frame, text="1. View All Students", width=25, command=view_all)
btn2 = tk.Button(frame, text="2. View Individual Student", width=25, command=view_individual)
btn3 = tk.Button(frame, text="3. Show Highest Score", width=25, command=show_highest)
btn4 = tk.Button(frame, text="4. Show Lowest Score", width=25, command=show_lowest)

btn1.grid(row=0, column=0, padx=5, pady=5)
btn2.grid(row=1, column=0, padx=5, pady=5)
btn3.grid(row=2, column=0, padx=5, pady=5)
btn4.grid(row=3, column=0, padx=5, pady=5)

text_box = tk.Text(root, width=70, height=20)
text_box.pack(pady=10)

root.mainloop()