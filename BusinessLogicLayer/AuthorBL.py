from DataAccessLayer import *


class AuthorVD:
    def __init__(self, author: Model.Author):
        self.Author = author

    def check_form(self):
        err = 0
        if len(self.Author.AuthorCode) == 0:
            msg.showerror('Validation Failed', 'Enter the AuthorCode!')
            err += 1
        if len(self.Author.FirstName) > 20 or len(self.Author.LastName) > 20:
            msg.showerror('Validation Failed', 'The name must be less than 20 Letters!')
            err += 1
        if not self.Author.FirstName.isalpha() or not self.Author.LastName.isalpha():
            msg.showerror('Validation Failed', 'Name Entry is Mandatory:The name should be just letter !')
            err += 1
        if self.Author.Phone.isalpha():
            msg.showerror('Validation Failed', 'The Phone should be just Number !')
            err += 1
        if len(self.Author.PostalCode) > 0:
            if len(self.Author.PostalCode) > 12 or not self.Author.PostalCode.isnumeric():
                msg.showerror('Validation Failed', 'The PostalCode should be just Number and less than 12 digit!')
                err += 1

        if err == 0:
            author_db = AuthorDB(self.Author)
            author_db.insert_author()
