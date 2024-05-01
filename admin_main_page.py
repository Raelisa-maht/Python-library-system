# Author : <Alyssa Mahtani Kaiting>
# Admin No / Grp : <230153R / 01>


from tkinter import *
import tkinter.font as font
from tkinter import simpledialog, messagebox

class Book:
    def __init__(self, isbn, title, book_type, quantity):
        self.isbn = isbn
        self.title = title
        self.book_type = book_type
        self.quantity = quantity

# Creating an empty list to store books
books = []

# Adding some initial books
books.append(Book("978-0134846019", "Data Analytics with Spark Using Python", "Paper Back", 6))
books.append(Book("978-0133316032", "Children's Reading", "eBook", 3))
books.append(Book("978-1292100142", "Global Marketing, 7th Edition", "eBook", 8))
books.append(Book("978-1587147029", "CCNA Cyber Ops SECFND #210-250 Official Cert Guide", "Non-Fiction", 5))
books.append(Book("0306406152", "Learn Data Analytics in 100 days", "Paper Back", 10))

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        myFont = font.Font(size=15, weight='bold')

        add_button = Button(self, text="Add Book", height=2, width=20, bg='green', command=self.add_book)
        add_button['font'] = myFont
        add_button.place(relx=0.5, rely=0.3, anchor=CENTER)

        remove_button = Button(self, text="Remove Book", height=2, width=20, bg='orange', command=self.remove_book)
        remove_button['font'] = myFont
        remove_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        update_button = Button(self, text="Update Book", height=2, width=20, bg='yellow', command=self.update_book)
        update_button['font'] = myFont
        update_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        search_button = Button(self, text="Search", height=2, width=20, bg='purple', command=self.search_book)
        search_button['font'] = myFont
        search_button.place(relx=0.5, rely=0.1, anchor=CENTER)

        exit_button = Button(self, text="Exit", height=2, width=20, bg='red', command=self.exit_program)
        exit_button['font'] = myFont
        exit_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    def add_book(self):
        entry_window = Toplevel(self.master)  # Create a new top-level window for book entry

        isbn_label = Label(entry_window, text="ISBN:")
        isbn_label.pack()
        isbn_entry = Entry(entry_window)
        isbn_entry.pack()

        title_label = Label(entry_window, text="Book Title:")
        title_label.pack()
        title_entry = Entry(entry_window)
        title_entry.pack()

        book_type_label = Label(entry_window, text="Book Type:")
        book_type_label.pack()
        book_type_entry = Entry(entry_window)
        book_type_entry.pack()

        quantity_label = Label(entry_window, text="Quantity:")
        quantity_label.pack()
        quantity_entry = Entry(entry_window)
        quantity_entry.pack()

        def save_book():
            isbn = isbn_entry.get()
            title = title_entry.get()
            book_type = book_type_entry.get()
            quantity = quantity_entry.get()
            book = Book(isbn, title, book_type, quantity)
            books.append(book)
            messagebox.showinfo("Success", "Book added successfully!")
            entry_window.destroy()

        save_button = Button(entry_window, text="Save", command=save_book)
        save_button.pack()

    def remove_book(self):
        self.view_data()
        isbn = simpledialog.askstring("Remove Book", "Enter the ISBN of the book you want to remove:")
        if isbn is None:
            return

        for book in books:
            if book.isbn == isbn:
                books.remove(book)
                messagebox.showinfo("Success", "Book removed successfully!")
                return

        messagebox.showerror("Error", "Book not found.")

    def update_book(self):
        isbn = simpledialog.askstring("Update Book", "Enter the ISBN of the book you want to update:")
        if isbn is None:
            return

        for book in books:
            if book.isbn == isbn:
                update_window = Toplevel(self.master)  # Create a new top-level window for book update

                isbn_label = Label(update_window, text="ISBN:")
                isbn_label.pack()
                isbn_entry = Entry(update_window)
                isbn_entry.pack()
                isbn_entry.insert(0, book.isbn)  # Populate current ISBN

                title_label = Label(update_window, text="Book Title:")
                title_label.pack()
                title_entry = Entry(update_window)
                title_entry.pack()
                title_entry.insert(0, book.title)  # Populate current title

                book_type_label = Label(update_window, text="Book Type:")
                book_type_label.pack()
                book_type_entry = Entry(update_window)
                book_type_entry.pack()
                book_type_entry.insert(0, book.book_type)  # Populate current book type

                quantity_label = Label(update_window, text="Quantity:")
                quantity_label.pack()
                quantity_entry = Entry(update_window)
                quantity_entry.pack()
                quantity_entry.insert(0, book.quantity)  # Populate current quantity

                def update_details():
                    updated_isbn = isbn_entry.get()
                    updated_title = title_entry.get()
                    updated_book_type = book_type_entry.get()
                    updated_quantity = quantity_entry.get()

                    book.isbn = updated_isbn
                    book.title = updated_title
                    book.book_type = updated_book_type
                    book.quantity = int(updated_quantity)

                    update_window.destroy()
                    messagebox.showinfo("Success", "Book details updated successfully!")

                update_button = Button(update_window, text="Update", command=update_details)
                update_button.pack()

                return

        messagebox.showerror("Error", "Book not found.")

    def view_data(self):
        if len(books) == 0:
            messagebox.showinfo("Book List", "No books found.")
        else:
            book_list = "Book List:\n\n"
            for book in books:
                book_list += f"ISBN: {book.isbn}\n"
                book_list += f"Title: {book.title}\n"
                book_list += f"Book Type: {book.book_type}\n"
                book_list += f"Quantity: {book.quantity}\n"
                book_list += "-" * 30 + "\n"
            messagebox.showinfo("Book List", book_list)

    def search_book(self):
        keyword = simpledialog.askstring("Search Books", "Enter the keyword to search:")
        if keyword is None:
            return

        results = []
        for book in books:
            if keyword.lower() in book.isbn.lower() or keyword.lower() in book.title.lower() or keyword.lower() in book.book_type.lower():
                results.append(book)

        if len(results) == 0:
            messagebox.showinfo("Search Results", "No matching books found.")
        else:
            book_list = "Search Results:\n\n"
            for book in results:
                book_list += f"ISBN: {book.isbn}\n"
                book_list += f"Title: {book.title}\n"
                book_list += f"Book Type: {book.book_type}\n"
                book_list += f"Quantity: {book.quantity}\n"
                book_list += "-" * 30 + "\n"
            messagebox.showinfo("Search Results", book_list)

    def show_goodbye_message(self):
        messagebox.showinfo("Goodbye", "Exiting the Mini Library Application. Goodbye!")
    def exit_program(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.show_goodbye_message()
            self.master.destroy()

# Create the Tkinter window
root = Tk()
root.geometry("600x480")
root.title("Admin Portal")

# Create an instance of the Window class
app = Window(root)

# Start the Tkinter event loop
root.mainloop()
