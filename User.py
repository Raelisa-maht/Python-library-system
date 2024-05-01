# Author : <Alyssa Mahtani Kaiting>
# Admin No / Grp : <230153R / 01>



import tkinter.font as font
from tkinter import *

root = Tk()  # create parent window
root.geometry("600x480")  # Set the geometry of the frame
root.resizable(False, False)  # Set the resizable property to False

myFont = font.Font(size=15, weight='bold')  # Define font

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        text = Label(self, text="Please select user:")
        text['font'] = myFont
        text.place(relx=0.5, rely=0.1, anchor=CENTER)

app = Window(root)
root.wm_title("User")

def admin_mode():
    import admin_login
    print("Welcome to admin mode!")

def Student_mode():
    import student_login
    print("Welcome to Student mode!")

# Use Button widgets to create a simple UI
Student = Button(root, text="Student", height=2, width=10, bg='blue', command=Student_mode)
Student['font'] = myFont
Student.place(relx=0.30, rely=0.5, anchor=CENTER)

Admin = Button(root, text="Admin", height=2, width=10, bg='red', command=admin_mode)
Admin['font'] = myFont
Admin.place(relx=0.70, rely=0.5, anchor=CENTER)

root.mainloop()
