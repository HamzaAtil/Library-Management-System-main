from tkinter import *
from PIL import ImageTk, Image

# Initialize the root window
root = Tk()
root.title("Return Book")
root.geometry("600x500")
root.resizable(0, 0)

# Background Image
bg = ImageTk.PhotoImage(Image.open("/Users/arnavbatra/Library-Management-System/images/image.png"))
myLabel = Label(root, image=bg)
myLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for the return book form
myFrame = LabelFrame(root, bg="#3b404e", text="Return Book", bd=3, fg="white", padx=20, pady=20, labelanchor="n", font=("Calibri", 16, "bold"))
myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.8, anchor=CENTER)

# Style for Entry fields
entry_style = {
    "highlightbackground": "#3b404e",
    "bg": "#5c6173",
    "borderwidth": 2,
    "fg": "white",
    "font": ("Calibri", 12),
    "relief": FLAT,
}

# Name of Book Label and Entry
Label(myFrame, text="Book Name:", fg="white", bg="#3b404e", font=("Calibri", 12)).grid(row=0, column=0, padx=15, pady=10, sticky=W)
book_name_Enter = Entry(myFrame, **entry_style)
book_name_Enter.grid(row=0, column=1, padx=15, pady=10, sticky=W)

# Name of Author Label and Entry
Label(myFrame, text="Name of Author:", fg="white", bg="#3b404e", font=("Calibri", 12)).grid(row=1, column=0, padx=15, pady=10, sticky=W)
author_name_Enter = Entry(myFrame, **entry_style)
author_name_Enter.grid(row=1, column=1, padx=15, pady=10, sticky=W)

# Book ID Label and Entry
Label(myFrame, text="Book ID:", fg="white", bg="#3b404e", font=("Calibri", 12)).grid(row=2, column=0, padx=15, pady=10, sticky=W)
book_id_Enter = Entry(myFrame, **entry_style)
book_id_Enter.grid(row=2, column=1, padx=15, pady=10, sticky=W)

# Category Label and Entry
Label(myFrame, text="Category:", fg="white", bg="#3b404e", font=("Calibri", 12)).grid(row=3, column=0, padx=15, pady=10, sticky=W)
category_name_Enter = Entry(myFrame, **entry_style)
category_name_Enter.grid(row=3, column=1, padx=15, pady=10, sticky=W)

# Price Label and Entry
Label(myFrame, text="Price:", fg="white", bg="#3b404e", font=("Calibri", 12)).grid(row=4, column=0, padx=15, pady=10, sticky=W)
price_name_Enter = Entry(myFrame, **entry_style)
price_name_Enter.grid(row=4, column=1, padx=15, pady=10, sticky=W)

# Date Label and Entry
Label(myFrame, text="Date (DD/MM/YYYY):", fg="white", bg="#3b404e", font=("Calibri", 12)).grid(row=5, column=0, padx=15, pady=10, sticky=W)
date_name_Enter = Entry(myFrame, **entry_style)
date_name_Enter.grid(row=5, column=1, padx=15, pady=10, sticky=W)

# Rounded button
image = Image.open("/Users/arnavbatra/Library-Management-System/images/R.png")
image = image.resize((110, 40), Image.ANTIALIAS)
rounded = ImageTk.PhotoImage(image)

# Return Button
returnButton = Button(myFrame, image=rounded, borderwidth=0, highlightthickness=0)
returnButton.grid(row=6, column=0, columnspan=2, pady=20)

# Run the main loop
root.mainloop()
