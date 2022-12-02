from tkinter import *
from BusinessLogicLayer import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry


class RegisterOrderUI:
    def __init__(self):
        pass

    def form_load(self):
        orderfrm = Tk()
        orderfrm.title('New Order')
        orderfrm.geometry('300x230')
        orderfrm.resizable(None, None)
        position_right = int(orderfrm.winfo_screenwidth() / 2 - 300 / 2)
        position_down = int(orderfrm.winfo_screenheight() / 2 - 230 / 2)
        orderfrm.geometry("+{}+{}".format(position_right, position_down))

        book_db = BookDB()
        book_list = book_db.get_book_list()

        def back_to_main():
            orderfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            main_ui = MainUI()
            main_ui.form_load()

        def insert_order_command():
            book_id = txt_book_id.get().split(' ')[0]
            order_date = txt_order_date.get()
            quantity = txt_quantity.get()

            order = Model.Order(book_id, order_date, quantity)
            order_vd = OrderVD(order)
            order_vd.check_form()
            # order_db = OrderDB(order)
            # order_db.insertOrder()

        frameinfo = LabelFrame(orderfrm, text='  Order ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        lbl_book_id = Label(frameinfo, text='Book: ')
        lbl_book_id.grid(row=1, column=0, padx=10, pady=0, sticky='w')
        txt_book_id = StringVar()
        cmb_book_id = Combobox(frameinfo, width=20, textvariable=txt_book_id, state='readonly')
        cmb_book_id['values'] = book_list
        cmb_book_id.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        cmb_book_id.current()

        lbl_order_date = Label(frameinfo, text='Order Date: ')
        lbl_order_date.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txt_order_date = StringVar()
        ent_order_date = DateEntry(frameinfo, textvariable=txt_order_date, width=15, year=2021, month=1, day=1,
                                   background='DarkBlue', foreground='white', borderwidth=1, relief='solid',
                                   font='tahoma 10')
        ent_order_date.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        lbl_order_date_hint = Label(frameinfo, text='(Sample: YYYY/MM/DD)')
        lbl_order_date_hint.grid(row=3, column=1, padx=10, pady=0, sticky='w')

        lbl_quantity = Label(frameinfo, text='Quantity: ')
        lbl_quantity.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txt_quantity = StringVar()
        ent_quantity = Entry(frameinfo, textvariable=txt_quantity, width=20, highlightthickness=1)
        ent_quantity.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        btn_register = Button(orderfrm, text='Save', width=15, relief='groove', command=insert_order_command)
        btn_register.grid(row=5, column=0, padx=30, pady=10, sticky='w')

        btn_back = Button(orderfrm, text='Back to Main', width=15, relief='groove', command=back_to_main)
        btn_back.grid(row=5, column=0, padx=30, pady=10, sticky='e')

        orderfrm.mainloop()
