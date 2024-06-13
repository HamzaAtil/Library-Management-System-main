from tkinter import *
from PIL import ImageTk, Image
import backend

# Initialize the root window
root = Tk()
root.title("Library Management System")
root.geometry("600x500")
root.resizable(0, 0)

# Background Image
bg = ImageTk.PhotoImage(Image.open("images/image.png"))
myLabel = Label(root, image=bg)
myLabel.place(x=0, y=0, relwidth=1, relheight=1)

# New Frame for the buttons
myFrame = LabelFrame(root, bg="#2e2e2e", text="Welcome to the Library", bd=5, fg="#ffd700", padx=10, pady=15, font=("Helvetica", 14, "bold"), labelanchor="s")
myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.7, anchor=CENTER)


# Common button styles
button_style = {
    "fg": "#FFFFFF",
    "bg": "#3b404e",
    "relief": GROOVE,
    "highlightbackground": "#3b404e",
    "highlightthickness": 2,
    "highlightcolor": "#3b404e",
    "width": 20,
    "height": 2
}

# Adding buttons to the frame
buttons = [
    ("Add Book", 0),
    ("Delete Book", 1),
    ("View Book", 2),
    ("Issue Book", 3),
    ("Return Book", 4),
    ("Book Defaulters", 5)
]

for text, row in buttons:
    button = Button(myFrame, text=text, **button_style)
    button.grid(row=row, padx=20, pady=8, sticky="nesw")

# Run the main loop
root.mainloop()
