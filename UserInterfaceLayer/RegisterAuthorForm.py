from tkinter import *
from DataAccessLayer import *
from BusinessLogicLayer import *
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from Model import *
from tkinter.ttk import Combobox


class RegisterAuthorUI:
    def __init__(self):
        pass

    def form_load(self):
        authorfrm = Tk()
        authorfrm.title('Register an Author')
        authorfrm.geometry('300x420')
        authorfrm.resizable(None, None)
        position_right = int(authorfrm.winfo_screenwidth() / 2 - 300 / 2)
        position_down = int(authorfrm.winfo_screenheight() / 2 - 420 / 2)
        authorfrm.geometry("+{}+{}".format(position_right, position_down))

        def back_to_main():
            authorfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            main_ui = MainUI()
            main_ui.form_load()

        def insert_author_command():
            author_code = txt_author_code.get()
            firstname = txt_firstname.get()
            lastname = txt_lastname.get()
            phone = txt_phone.get()
            address = txt_address.get()
            city = txt_city.get()
            province = txt_province.get()
            postal_code = txt_postal_code.get()

            author = Model.Author(author_code, firstname, lastname, phone, address, city, province, postal_code)
            auther_vd = AuthorVD(author)
            auther_vd.check_form()
            # authordb = AuthorDB(author)
            # authordb.insertAuthor()

        frameinfo = LabelFrame(authorfrm, text=' Author Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        lbl_author_code = Label(frameinfo, text='Author Code: ')
        lbl_author_code.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txt_author_code = StringVar()
        txt_author_code = Entry(frameinfo, textvariable=txt_author_code, width=20, highlightthickness=1)
        txt_author_code.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lbl_firstname = Label(frameinfo, text='FirstName: ')
        lbl_firstname.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txt_firstname = StringVar()
        ent_firstname = Entry(frameinfo, textvariable=txt_firstname, width=20, highlightthickness=1)
        ent_firstname.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lbl_lastname = Label(frameinfo, text='LastName: ')
        lbl_lastname.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txt_lastname = StringVar()
        ent_lastname = Entry(frameinfo, textvariable=txt_lastname, width=20, highlightthickness=1)
        ent_lastname.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lbl_phone = Label(frameinfo, text='Phone: ')
        lbl_phone.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txt_phone = StringVar()
        ent_phone = Entry(frameinfo, textvariable=txt_phone, width=20, highlightthickness=1)
        ent_phone.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        lbl_address = Label(frameinfo, text='Address: ')
        lbl_address.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txt_address = StringVar()
        ent_address = Entry(frameinfo, textvariable=txt_address, width=20, highlightthickness=1)
        ent_address.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        lbl_city = Label(frameinfo, text='City: ')
        lbl_city.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        txt_city = StringVar()
        ent_city = Entry(frameinfo, textvariable=txt_city, width=20, highlightthickness=1)
        ent_city.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        lbl_province = Label(frameinfo, text='Province: ')
        lbl_province.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        txt_province = StringVar()
        ent_province = Entry(frameinfo, textvariable=txt_province, width=20, highlightthickness=1)
        ent_province.grid(row=7, column=1, padx=10, pady=10, sticky='w')

        lbl_postal_code = Label(frameinfo, text='PostalCode: ')
        lbl_postal_code.grid(row=8, column=0, padx=10, pady=10, sticky='w')
        txt_postal_code = StringVar()
        ent_postal_code = Entry(frameinfo, textvariable=txt_postal_code, width=20, highlightthickness=1)
        ent_postal_code.grid(row=8, column=1, padx=10, pady=10, sticky='w')

        btn_register_author = Button(authorfrm, text='Register', width=12, relief='groove',
                                     command=insert_author_command)
        btn_register_author.grid(row=9, column=0, padx=30, pady=10, sticky='w')

        btn_back = Button(authorfrm, text='Back to Main', width=12, relief='groove', command=back_to_main)
        btn_back.grid(row=9, column=0, padx=30, pady=10, sticky='e')

        authorfrm.mainloop()
