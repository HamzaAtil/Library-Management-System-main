from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import backend

root = Tk()
root.title("Login")
root.geometry("600x500")
root.resizable(0, 0)

# Background Image
bg = ImageTk.PhotoImage(Image.open("images/image.png"))
myLabel = Label(root, image=bg)
myLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for the login form
myFrame = LabelFrame(root, bg="#3b404e", text="Account Login", bd=3, fg="white", padx=20, pady=20, labelanchor="n", font=("Calibri", 16, "bold"))
myFrame.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6, anchor=CENTER)

# Style for Entry fields
entry_style = {
    "highlightbackground": "#3b404e",
    "bg": "#5c6173",
    "borderwidth": 2,
    "fg": "white",
    "font": ("Calibri", 12),
    "relief": FLAT,
}

# User ID Label
ID = Label(myFrame, text="Username:", fg="white", bg="#3b404e", font=("Calibri", 12), padx=10, pady=10)
ID.grid(row=0, column=0, padx=15, pady=15, sticky=W)

# User Password Label
Password = Label(myFrame, text="Password:", fg="white", bg="#3b404e", font=("Calibri", 12), padx=10, pady=10)
Password.grid(row=1, column=0, padx=15, pady=15, sticky=W)

# User ID field
idEnter = Entry(myFrame, **entry_style)
idEnter.grid(row=0, column=1, padx=15, pady=15)

# User Password field
passEnter = Entry(myFrame, **entry_style, show="*")
passEnter.grid(row=1, column=1, padx=15, pady=15)

# Rounded button image
image = Image.open("images/R.png")
image = image.resize((110, 40), Image.ANTIALIAS)
rounded = ImageTk.PhotoImage(image)

# Login function
def value():
    idval = idEnter.get()
    passval = passEnter.get()
    out = backend.login_data(idval, passval) #fct return 0 ou 1
    if out == 1:
        messagebox.showinfo("Success", "Welcome")
    else:
        messagebox.showinfo("Failed", "Invalid Credentials")

# Login Button
loginButton = Button(myFrame, image=rounded, borderwidth=0, command=value, highlightthickness=0, relief=FLAT)
loginButton.grid(row=2, column=0, columnspan=2, pady=20)

# Registration button
register = Button(myFrame, text="Create new account", fg="white", bg="#3b404e", relief=FLAT, font=("Calibri", 10, "underline"), highlightthickness=0, cursor="hand2")
register.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
