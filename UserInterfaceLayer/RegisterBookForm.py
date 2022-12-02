from tkinter import *
from DataAccessLayer import *
from tkinter import messagebox as msg, filedialog
from UserInterfaceLayer import *
from BusinessLogicLayer import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry


class RegisterBookUI:
    def __init__(self):
        pass

    def form_load(self):
        bookfrm = Tk()
        bookfrm.title('Register a Book')
        bookfrm.geometry('350x450')
        bookfrm.resizable(None, None)
        position_right = int(bookfrm.winfo_screenwidth() / 2 - 350 / 2)
        position_down = int(bookfrm.winfo_screenheight() / 2 - 450 / 2)
        bookfrm.geometry("+{}+{}".format(position_right, position_down))

        author_db = AuthorDB()
        author_list = author_db.get_author_list()

        def back_to_main():
            bookfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            main_ui = MainUI()
            main_ui.form_load()

        def insert_book_command():
            book_name = txt_book_name.get()
            book_code = txt_book_code.get()
            author_id = txt_author_id.get().split(' ')[0]
            book_type = txt_book_type .get()
            price = txt_price.get()
            isbn = txt_isbn.get()
            publish_date = txt_publish_date.get()
            paperback = txt_paperback.get()

            book = Model.Book(book_name, book_code, author_id, book_type, price, isbn, publish_date, paperback)
            book_vd = BookVD(book)
            book_vd.check_form()
            # book_db = BookDB(book)
            # book_db.insertBook()

        frameinfo = LabelFrame(bookfrm, text=' Book Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        lbl_book_name = Label(frameinfo, text='BookName: ')
        lbl_book_name.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txt_book_name = StringVar()
        ent_book_name = Entry(frameinfo, textvariable=txt_book_name, width=20, highlightthickness=1)
        ent_book_name.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lbl_book_code = Label(frameinfo, text='BookCode: ')
        lbl_book_code.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txt_book_code = StringVar()
        ent_book_code = Entry(frameinfo, textvariable=txt_book_code, width=20, highlightthickness=1)
        ent_book_code.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lbl_author_id = Label(frameinfo, text='Author: ')
        lbl_author_id.grid(row=3, column=0, padx=10, pady=0, sticky='w')

        txt_author_id = StringVar()
        cmb_author_id = Combobox(frameinfo, width=20, textvariable=txt_author_id, state='readonly')
        cmb_author_id['values'] = author_list
        cmb_author_id.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        cmb_author_id.current()

        lbl_book_type = Label(frameinfo, text='BookType : ')
        lbl_book_type.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txt_book_type = StringVar()
        cmb_book_type = Combobox(frameinfo, width=20, textvariable=txt_book_type, state='readonly')
        array_book_type = []

        with open('DB/BookTypes.csv', mode='r', encoding='utf-8') as myFile:
            for line in myFile.readlines():
                temp = line.rstrip('\n')
                array_book_type.append(temp)
        cmb_book_type['values'] = array_book_type
        cmb_book_type.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        cmb_book_type.current()

        lbl_price = Label(frameinfo, text='Price: ')
        lbl_price.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txt_price = StringVar()
        ent_price = Entry(frameinfo, textvariable=txt_price, width=20, highlightthickness=1)
        ent_price.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        lbl_isbn = Label(frameinfo, text='ISBN: ')
        lbl_isbn.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        txt_isbn = StringVar()
        ent_isbn = Entry(frameinfo, textvariable=txt_isbn, width=20, highlightthickness=1)
        ent_isbn.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        lbl_publish_date = Label(frameinfo, text='Publish Date: ')
        lbl_publish_date.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        txt_publish_date = StringVar()
        ent_publish_date = DateEntry(frameinfo, textvariable=txt_publish_date, width=15, year=2021, month=1, day=1,
                                     background='darkblue', foreground='white', borderwidth=1, relief='solid',
                                     font='tahoma 10')
        ent_publish_date.grid(row=7, column=1, padx=10, pady=10, sticky='w')
        lbl_publish_date_hint = Label(frameinfo, text='(Sample: YYYY/MM/DD)')
        lbl_publish_date_hint.grid(row=8, column=1, padx=10, pady=0, sticky='w')

        def get_file_path():
            photo_path = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                    filetype=(("jpeg files", "*.jpg"), ("PNG Files", "*.png"),
                                                              ("all files", "*.*")))
            if photo_path is not None:
                txt_paperback.set(photo_path)

        lbl_paperback = Label(frameinfo, text='Paperback:')
        lbl_paperback.grid(row=9, column=0, padx=10, pady=10, sticky='w')
        txt_paperback = StringVar()
        ent_paperback = Entry(frameinfo, textvariable=txt_paperback, width=17, font='tahoma 11')
        ent_paperback.grid(row=9, column=1, padx=10, pady=10)
        btn_paperback = Button(frameinfo, width=3, text='...', borderwidth=2, command=get_file_path)
        btn_paperback.grid(row=9, column=2, padx=5, pady=10)

        btn_register = Button(bookfrm, text='Register ', width=15, relief='groove', command=insert_book_command)
        btn_register.grid(row=10, column=0, padx=30, pady=10, sticky='w')

        btn_back = Button(bookfrm, text='Back to Main', width=15, relief='groove', command=back_to_main)
        btn_back.grid(row=10, column=0, padx=30, pady=10, sticky='e')

        bookfrm.mainloop()
