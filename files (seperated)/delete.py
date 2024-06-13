from tkinter import *
from PIL import ImageTk, Image
import backend

# Creating window, giving title and size
root = Tk()
root.title("Delete Book")
root.geometry("600x500")
root.resizable(0, 0)

# Putting background image
back_ground = ImageTk.PhotoImage(Image.open("images/image.png"))
back_ground_label = Label(root, image=back_ground)
back_ground_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for delete book
frame_1 = LabelFrame(root, bg="#3b404e", text="Delete Book", bd=3, fg="white", padx=20, pady=20, labelanchor="n", font=("Calibri", 16, "bold"))
frame_1.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6, anchor=CENTER)

# Style for Entry fields
entry_style = {
    "highlightbackground": "#3b404e",
    "bg": "#5c6173",
    "borderwidth": 2,
    "fg": "white",
    "font": ("Calibri", 12),
    "relief": FLAT,
}

# Delete function
def delete():
    # Get entry values
    sno_val = entry_box_sno.get()
    book_name_val = entry_box_book.get()
    
    # Hide input fields and labels
    sno.grid_forget()
    entry_box_sno.grid_forget()
    name_book.grid_forget()
    entry_box_book.grid_forget()
    next_button.grid_forget()
    
    # Delete book from backend
    backend.delete_book(sno_val, book_name_val)

    # Display success message
    success_label = Label(frame_1, text=f"\n\nSerial no. : {sno_val}\nBook Name : {book_name_val}\nis successfully deleted from the record.", 
                          fg="white", bg="#3b404e", font=("Calibri", 12), width=35, anchor="center")
    success_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
    
    # Next button for going to the next step
    next_button_1 = Button(frame_1, image=rounded_button, borderwidth=0)
    next_button_1.grid(row=1, column=0, columnspan=2, pady=30)
    next_button_1.config(highlightthickness=0)

# Label asking for serial number of book
sno = Label(frame_1, text="Serial No. :", fg="white", bg="#3b404e", font=("Calibri", 12))
sno.grid(row=0, column=0, padx=20, pady=15, sticky=E)

# Entry box to type the serial number of book
entry_box_sno = Entry(frame_1, **entry_style)
entry_box_sno.grid(row=0, column=1, padx=20, pady=15, sticky=W)

# Label asking for name of book
name_book = Label(frame_1, text="Name of Book :", fg="white", bg="#3b404e", font=("Calibri", 12))
name_book.grid(row=1, column=0, padx=20, pady=15, sticky=E)

# Entry box to type the name of book
entry_box_book = Entry(frame_1, **entry_style)
entry_box_book.grid(row=1, column=1, padx=20, pady=15, sticky=W)

# Importing button image, resizing it, creating an alias name
button_image = Image.open("images/R.png")
button_image = button_image.resize((110, 40), Image.ANTIALIAS)
rounded_button = ImageTk.PhotoImage(button_image)

# Next button for going to the next step
next_button = Button(frame_1, image=rounded_button, borderwidth=0, command=delete)
next_button.grid(row=2, column=0, columnspan=2, pady=30)
next_button.config(highlightthickness=0)

root.mainloop()
