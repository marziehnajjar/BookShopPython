from DataAccessLayer import *


class BookVD:
    def __init__(self, book: Model.Book):
        self.Book = book

    def check_form(self):
        err = 0
        if len(self.Book.BookName) == 0:
            msg.showerror('Validation Failed', 'Enter the Book name!')
            err += 1
        if len(self.Book.AuthorID) == 0:
            msg.showerror('Validation Failed', 'Enter the Author!')
            err += 1
        if len(self.Book.BookCode) == 0:
            msg.showerror('Validation Failed', 'Enter the Book code!')
            err += 1
        if len(self.Book.BookType) == 0:
            msg.showerror('Validation Failed', 'Enter the BookType!')
            err += 1
        if len(self.Book.Price) == 0:
            msg.showerror('Validation Failed', 'Enter the Price!')
            err += 1
        if len(self.Book.ISBN) == 0:
            msg.showerror('Validation Failed', 'Enter the ISBN!')
            err += 1

        if not self.Book.Price.isnumeric():
            msg.showerror('Validation Failed', 'The Price should be just Number !')
            err += 1

        if err == 0:
            book_db = BookDB(self.Book)
            book_db.insert_book()
