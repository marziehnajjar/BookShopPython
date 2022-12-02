from tkinter import *
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from Model import *


class MainUI:
    def __init__(self):
        pass

    def form_load(self):
        mainfrm = Tk()
        mainfrm.title('Main Form')
        mainfrm.geometry('320x340')
        mainfrm.resizable(None, None)
        position_right = int(mainfrm.winfo_screenwidth() / 2 - 320 / 2)
        position_down = int(mainfrm.winfo_screenheight() / 2 - 340 / 2)
        mainfrm.geometry("+{}+{}".format(position_right, position_down))

        # region Functions ...
        def register_book_formload():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterBookForm import RegisterBookUI
            register_book_form = RegisterBookUI()
            register_book_form.form_load()

        def register_author_formload():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterAuthorForm import RegisterAuthorUI
            register_author_form = RegisterAuthorUI()
            register_author_form.form_load()

        def register_order_formload():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterOrderForm import RegisterOrderUI
            register_order_form = RegisterOrderUI()
            register_order_form.form_load()

        def show_about_us():
            msg.showinfo('Final Quiz', 'Student : Marzieh Najjar\nPython9911')

        # endregion

        # region Icon ...
        img_register_book = PhotoImage(file='UserInterfaceLayer/icon/001-open-book.png')
        img_register_author = PhotoImage(file='UserInterfaceLayer/icon/002-writer.png')
        img_register_order = PhotoImage(file='UserInterfaceLayer/icon/003-checklist.png')
        img_about_us = PhotoImage(file='UserInterfaceLayer/icon/info.png')

        # endregion

        frameinfo = LabelFrame(mainfrm, text=' Book Shop ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        btn_book = Button(frameinfo, text='Add Book', image=img_register_book, compound=TOP, pady=10,
                          height=100, width=100, relief='groove', font='tahoma 10 bold',
                          command=register_book_formload)
        btn_book.grid(row=1, column=0, padx=10, pady=10)

        btn_author = Button(frameinfo, text='Add Author', image=img_register_author, compound=TOP, pady=10,
                            height=100, width=100, relief='groove', font='tahoma 10 bold',
                            command=register_author_formload)
        btn_author.grid(row=1, column=1, padx=10, pady=10)

        btn_order = Button(frameinfo, text='Add Order', image=img_register_order, compound=TOP, pady=10,
                           height=100, width=100, relief='groove', font='tahoma 10 bold',
                           command=register_order_formload)
        btn_order.grid(row=2, column=0, padx=10, pady=10)

        btn_about_us = Button(frameinfo, text='About Us', image=img_about_us, compound=TOP, pady=10, height=100,
                              width=100, relief='groove', font='tahoma 10 bold', command=show_about_us)
        btn_about_us.grid(row=2, column=1, padx=20, pady=10)

        mainfrm.mainloop()
