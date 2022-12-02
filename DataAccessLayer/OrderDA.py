import sqlite3
import Model.AuthorModel
from tkinter import messagebox as msg


class OrderDB:
    def __init__(self, order: Model.Order = None):
        self.Order = order

    def insert_order(self):
        db_name = './DB/BookStore.db'
        query = 'INSERT INTO Sales(BookID,OrderDate,Quantity)' \
                'VALUES(?,?,?)'
        params = (self.Order.BookID, self.Order.OrderDate, self.Order.Quantity)

        try:
            with sqlite3.Connection(db_name) as connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                msg.showinfo('Database', 'Added Successfully.')
        except ConnectionError:
            msg.showerror('Database', 'Unexpected failure. Error: ' + ConnectionError.strerror)

        finally:
            connection.close()
