# Author : <Alyssa Mahtani Kaiting>
# Admin No / Grp : <230153R / 01>



import tkinter as tk
from tkinter import messagebox
from student_login_logic import validate_student_login
 # Import the module for the student main page

def student_login():
    username = entry_username.get()
    password = entry_password.get()

    if validate_student_login(username, password):
        messagebox.showinfo("Login Successful", "Logged in as student!")
        window.destroy()
        import student_main_page
    else:
        messagebox.showerror("Login Failed", "Invalid student credentials")

# Create the student login window
window = tk.Tk()
window.title("Student Login")

# Create the username label and entry
label_username = tk.Label(window, text="Username:")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

# Create the password label and entry
label_password = tk.Label(window, text="Password:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create the login button
button_login = tk.Button(window, text="Login", command=student_login)
button_login.pack()

# Start the main event loop
window.mainloop()
