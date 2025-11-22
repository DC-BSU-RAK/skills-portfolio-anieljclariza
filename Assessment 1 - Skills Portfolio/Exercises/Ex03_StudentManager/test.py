import tkinter as tk
from tkinter import scrolledtext

# Create the main window
root = tk.Tk()
root.title("Display Text File")

# Create a scrolled text widget (Text widget with scrollbar)
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
text_area.pack(padx=10, pady=10)

# Read the file contents
file_path = r"Assessment 1 - Skills Portfolio\Exercises\Ex03_StudentManager\studentMarks.txt"  # Replace with your file path
with open(file_path, "r") as file:
    content = file.read()

# Insert the content into the text widget
text_area.insert(tk.END, content)

# Optional: make the text widget read-only
text_area.configure(state='disabled')

# Run the Tkinter event loop
root.mainloop()