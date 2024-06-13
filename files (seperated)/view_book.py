from tkinter import *
from PIL import ImageTk, Image

# Initialize the root window
root = Tk()
root.title('VIEW BOOK')
root.iconbitmap('/Users/apple/Downloads/library_icon.ico')
root.geometry("600x500")
root.resizable(0, 0)

# Background Image
back_image = ImageTk.PhotoImage(Image.open("/Users/apple/Library-Management-System/images/image.png"))
myLabel = Label(image=back_image)
myLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for the book list
main_Frame = LabelFrame(root, bg="#3b404e", text="View Book List", bd=3, fg="white", padx=5, pady=5, labelanchor="n", font=("Calibri", 16, "bold"))
main_Frame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.7, anchor=CENTER)

# Header Label
header_label = Label(main_Frame, text="%-10s%-20s%-20s%-10s" % ('S.No', 'Title', 'Author', 'Status'), bg="#3b404e", fg='white', font=("Calibri", 12, "bold"))
header_label.grid(pady=10, row=0, column=0, sticky="w")

# Separator Label
separator_label = Label(main_Frame, text="---------------------------------------------------------------", bg="#3b404e", fg='white')
separator_label.grid(pady=2, row=1, column=0, columnspan=4)

# Book List
my_list = [["1.", "Harry Potter", "J.K. Rowling", "Yes"], ["2.", "Invisible Man", "H.G. Wells", "Yes"], ["3.", "Dracula", "Bram S.", "Yes"], ["4.", "Beloved", "Toni M.", "Yes"]]

# Display Book List
y = 2
for i in my_list:
    book_label = Label(main_Frame, text="%-10s%-20s%-20s%-10s" % (i[0], i[1], i[2], i[3]), bg="#3b404e", fg='white', font=("Calibri", 12))
    book_label.grid(pady=5, row=y, column=0, sticky="w")
    y += 1

# Next Button
image = Image.open("/Users/apple/Library-Management-System/images/R.png")
image = image.resize((110, 40), Image.ANTIALIAS)
rounded = ImageTk.PhotoImage(image)

back_button = Button(main_Frame, image=rounded, borderwidth=0, anchor="center", highlightthickness=0)
back_button.grid(row=y, column=0, pady=15)

# Run the main loop
root.mainloop()
