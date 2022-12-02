import sqlite3
import Model.AuthorModel
from tkinter import messagebox as msg


class BookDB:
    def __init__(self, book: Model.Book = None):
        self.Book = book

    def get_book_list(self):
        db_name = './DB/BookStore.db'
        query = 'SELECT Books.ID , Books.BookName  FROM Books '

        try:
            with sqlite3.Connection(db_name) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                a = cursor.fetchall()
                connection.commit()
                return a
        except ConnectionError:
            pass

        finally:
            connection.close()

    def insert_book(self):
        db_name = './DB/BookStore.db'
        query = 'INSERT INTO Books(BookName,BookCode,BookType ,Price,ISBN, PublishDate, Paperback )' \
                'VALUES(?,?,?,?,?,?,?)'
        params = (self.Book.BookName, self.Book.BookCode, self.Book.BookType, self.Book.Price,
                  self.Book.ISBN, self.Book.PublishDate, self.Book.Paperback)

        try:
            with sqlite3.Connection(db_name) as connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                book_id = cursor.lastrowid
                author_id = self.Book.AuthorID
                query_book_author = 'INSERT INTO Book_Author(BookID,AuthorID) VALUES(?,?)'
                params_book_author = (book_id, author_id)
                cursor.execute(query_book_author, params_book_author)
                connection.commit()

                msg.showinfo('Database', 'Added Successfully.')
        except ConnectionError:
            msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)

        finally:
            connection.close()
