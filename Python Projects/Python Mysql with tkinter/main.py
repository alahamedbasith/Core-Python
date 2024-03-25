from tkinter import *
from tkinter.ttk import Combobox,Style,Treeview
from tkinter import messagebox
from database import Database

db = Database("Employee.db")


window = Tk()
window.title("Employee Management System")
window.geometry("1920x1080+0+0")
window.config(bg="#2c3e58")
window.state("zoomed")

# Entries Frame
entries_frame = Frame(window,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title = Label(entries_frame,text="Employee Management System",font=('Calibri',18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=20,pady=20)

# Variable Declaration

name = StringVar()
age = StringVar()
doj = StringVar()
email = StringVar()
gender = StringVar()
contact = StringVar()

# Name
lblname = Label(entries_frame,text="Name",font=('Calibri',16),bg="#535c68",fg="white")
lblname.grid(row=1,column=0,padx=10,pady=10,sticky="w")
textname = Entry(entries_frame,textvariable=name,font=('Calibri',16),width=30)
textname.grid(row=1,column=1,padx=10,pady=10,sticky="w")

# Age
lblage = Label(entries_frame,text="Age",font=('Calibri',16),bg="#535c68",fg="white")
lblage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
textage = Entry(entries_frame,textvariable=age,font=('Calibri',16),width=30)
textage.grid(row=1,column=3,padx=10,pady=10,sticky="w")

# doj
lbldoj = Label(entries_frame,text="D.O.J",font=('Calibri',16),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
textdoj = Entry(entries_frame,textvariable=doj,font=('Calibri',16),width=30)
textdoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

# Email
lblemail = Label(entries_frame,text="Email",font=('Calibri',16),bg="#535c68",fg="white")
lblemail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
textemail = Entry(entries_frame,textvariable=email,font=('Calibri',16),width=30)
textemail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

# Gender
lblgender = Label(entries_frame,text="Gender",font=('Calibri',16),bg="#535c68",fg="white")
lblgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
# To use dropdown use combobox
combogender = Combobox(entries_frame,font=('Calibri',16),width=28,textvariable=gender,state="readonly")
combogender['values'] = ("Male","Female")
combogender.grid(row=3,column=1,padx=10,pady=10,sticky="w")

# Contact
lblcontact = Label(entries_frame,text="Contact",font=('Calibri',16),bg="#535c68",fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
textcontact = Entry(entries_frame,textvariable=contact,font=('Calibri',16),width=30)
textcontact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

# Address
lbladdress = Label(entries_frame,text="Address",font=('Calibri',16),bg="#535c68",fg="white")
lbladdress.grid(row=4,column=0,padx=10,pady=10,sticky="w")
textaddress = Text(entries_frame,width=85,height=5,font=('Calibri',16))
textaddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

# This function for getting selected id using capture event
def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    
    # Set the values in the field 
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    textaddress.delete(1.0, END)
    textaddress.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children()) # For avoiding duplicates
    for row in db.fetch():
        tv.insert("", END, values=row)

def add_employee():
    if textname.get() == "" or textage.get() == "" or textdoj.get() == "" or textemail.get() == "" or combogender.get() == "" or textcontact.get() == "" or textaddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(textname.get(),textage.get(), textdoj.get() , textemail.get() ,combogender.get(), textcontact.get(), textaddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clear_employee()
    dispalyAll()
    
def update_employee():
    if textname.get() == "" or textage.get() == "" or textdoj.get() == "" or textemail.get() == "" or combogender.get() == "" or textcontact.get() == "" or textaddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],textname.get(),textage.get(), textdoj.get() , textemail.get() ,combogender.get(), textcontact.get(), textaddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Updated")
    clear_employee()
    dispalyAll()

def delete_employee():
    db.delete(row[0])
    clear_employee()
    dispalyAll()

def clear_employee():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")
    textaddress.delete(1.0,END)


# Button Frame
btn_frame = Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")

# Button Add
btn_add = Button(btn_frame,command=add_employee,text="Add Details",width=15,font=('Calibri',16),bg="#16a885",fg="white",bd=0)
# Button frame is seperate one,so row and column have seperate axis
btn_add.grid(row=0,column=0,padx=10)

# Button Edit
btn_edit = Button(btn_frame,command=update_employee,text="Update Details",width=15,font=('Calibri',16),bg="#2988b9",fg="white",bd=0)
btn_edit.grid(row=0,column=1,padx=10)

# Button Delete
btn_delete = Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=('Calibri',16),bg="#c8392b",fg="white",bd=0)
btn_delete.grid(row=0,column=2,padx=10)

# Button Clear
btn_clear = Button(btn_frame,command=clear_employee,text="Clear Details",width=15,font=('Calibri',16),bg="#f39c12",fg="white",bd=0)
btn_clear.grid(row=0,column=3,padx=10)


# Table Frame
tree_frame = Frame(window, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="D.O.B")
tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.column("6", width=10)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv['show'] = 'headings'

# Create the event capture
tv.bind("<ButtonRelease-1>", getData)

tv.pack(fill=X)

dispalyAll()

window.mainloop()