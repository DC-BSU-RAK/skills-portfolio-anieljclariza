import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Background Image Example")
root.geometry("600x400")

# Load and resize background image
bg_image = Image.open( r"Assessment 1 - Skills Portfolio\Exercises\Ex01_MathsQuiz\1.jpg")
bg_image = bg_image.resize((600, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

# Create label to display the background
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Keep a reference (important!)
bg_label.image = bg_photo

# Add other widgets on top
title = tk.Label(root, text="Welcome!", font=("Arial", 24), bg="gray")
title.place(relx=0.5, rely=0.1, anchor="center")

button = tk.Button(root, text="Click Me", font=("Arial", 14))
button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
