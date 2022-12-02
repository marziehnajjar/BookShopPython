from DataAccessLayer import *


class OrderVD:
    def __init__(self, order: Model.Order):
        self.Order = order

    def check_form(self):
        err = 0
        if len(self.Order.BookID) == 0:
            msg.showerror('Validation Failed', 'Enter the Book!')
            err += 1
        if len(self.Order.OrderDate) == 0:
            msg.showerror('Validation Failed', 'Enter the OrderDate!')
            err += 1
        if len(self.Order.Quantity) == 0:
            msg.showerror('Validation Failed', 'Enter the Quantity!')
            err += 1

        if not self.Order.Quantity.isnumeric():
            msg.showerror('Validation Failed', 'The Quantity should be just Number !')
            err += 1

        if err == 0:
            order_db = OrderDB(self.Order)
            order_db.insert_order()
