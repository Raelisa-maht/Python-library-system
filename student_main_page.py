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
        self.available = True

# Creating an empty list to store books
books = []

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        myFont = font.Font(size=15, weight='bold')


        borrow_button = Button(self, text="Borrow Book", height=2, width=20, bg='green', command=self.borrow_book)
        borrow_button['font'] = myFont
        borrow_button.place(relx=0.5, rely=0.25, anchor=CENTER)

        return_button = Button(self, text="Return Book", height=2, width=20, bg='orange', command=self.return_book)
        return_button['font'] = myFont
        return_button.place(relx=0.5, rely=0.4, anchor=CENTER)

        view_button = Button(self, text="View Books", height=2, width=20, bg='yellow', command=self.view_data)
        view_button['font'] = myFont
        view_button.place(relx=0.5, rely=0.55, anchor=CENTER)

        search_button = Button(self, text="Search Books", height=2, width=20, bg='purple', command=self.search_data)
        search_button['font'] = myFont
        search_button.place(relx=0.5, rely=0.1, anchor=CENTER)

        borrowed_button = Button(self, text="Borrowed Books", height=2, width=20, bg='light blue', command=self.borrowed_books)
        borrowed_button['font'] = myFont
        borrowed_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        exit_button = Button(self, text="Exit", height=2, width=20, bg='red', command=self.exit_program)
        exit_button['font'] = myFont
        exit_button.place(relx=0.5, rely=0.85, anchor=CENTER)

        # Adding some initial books
        books.append(Book("978-0134846019", "Data Analytics with Spark Using Python", "Paper Back", 6))
        books.append(Book("978-0133316032", "Children's Reading", "eBook", 3))
        books.append(Book("978-1292100142", "Global Marketing, 7th Edition", "eBook", 8))
        books.append(Book("978-1587147029", "CCNA Cyber Ops SECFND #210-250 Official Cert Guide", "Non-Fiction", 5))
        books.append(Book("0306406152", "Learn Data Analytics in 100 days", "Paper Back", 10))

    def borrow_book(self):
        isbn = simpledialog.askstring("Borrow Book", "Enter the ISBN of the book you want to borrow:")
        if isbn is None:
            return

        for book in books:
            if book.isbn == isbn:
                if book.available:
                    if book.quantity > 0:
                        book.quantity -= 1
                        book.available = False
                        messagebox.showinfo("Success", "Book borrowed successfully!")
                    else:
                        messagebox.showwarning("Unavailable", "No more copies of the book available.")
                else:
                    messagebox.showwarning("Unavailable", "Book is not available for borrowing.")
                return

        messagebox.showerror("Error", "Book with the entered ISBN not found.")

    def borrowed_books(self):
        borrowed_list = "Borrowed Books:\n\n"
        borrowed_books_count = 0

        for book in books:
            if not book.available:
                borrowed_list += f"ISBN: {book.isbn}\n"
                borrowed_list += f"Title: {book.title}\n"
                borrowed_list += f"Book Type: {book.book_type}\n"
                borrowed_list += "-" * 30 + "\n"
                borrowed_books_count += 1

        if borrowed_books_count == 0:
            messagebox.showinfo("Borrowed Books", "No books are currently borrowed.")
        else:
            messagebox.showinfo("Borrowed Books", borrowed_list)

    def return_book(self):
        isbn = simpledialog.askstring("Return Book", "Enter the ISBN of the book you want to return:")
        if isbn is None:
            return

        for book in books:
            if book.isbn == isbn:
                if not book.available:
                    book.quantity += 1
                    book.available = True
                    messagebox.showinfo("Success", "Book returned successfully!")
                else:
                    messagebox.showwarning("Already Available", "Book is already available.")
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


    def search_data(self):
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
root.title("Student Portal")

# Create an instance of the Window class
app = Window(root)

# Start the Tkinter event loop
root.mainloop()
