import sqlite3
import Model.AuthorModel
from tkinter import messagebox as msg


class AuthorDB:

    def __init__(self, author: Model.AuthorModel = None):
        self.Author = author

    def get_author_list(self):
        db_name = './DB/BookStore.db'
        query = 'SELECT Authors.ID , Authors.FirstName , Authors.LastName FROM Authors '

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

    def insert_author(self):
        db_name = './DB/BookStore.db'
        query = 'INSERT INTO Authors(AuthorCode,FirstName,LastName,Phone,Address, City, Province, PostalCode)' \
                'VALUES(?,?,?,?,?,?,?,?)'
        params = (self.Author.AuthorCode, self.Author.FirstName, self.Author.LastName, self.Author.Phone,
                  self.Author.Address, self.Author.city, self.Author.Province, self.Author.PostalCode)

        try:
            with sqlite3.Connection(db_name) as connection:
                cursor = connection.cursor()
                result = cursor.execute(query, params)
                connection.commit()
                msg.showinfo('Database', 'Added Successfully.')
        except ConnectionError:
            msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)

        finally:
            connection.close()
