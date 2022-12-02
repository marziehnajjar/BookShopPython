from tkinter import *
from tkinter import messagebox as msg


Loginfrm = Tk()
Loginfrm.title('Login Form')
Loginfrm.geometry('290x300')
Loginfrm.resizable(None, None)
positionRight = int(Loginfrm.winfo_screenwidth() / 2 - 290 / 2)
positionDown = int(Loginfrm.winfo_screenheight() / 2 - 300 / 2)
Loginfrm.geometry("+{}+{}".format(positionRight, positionDown))


def check_login():
    username = txtUserName.get()
    password = txtPassword.get()
    if username == 'admin' and password == 'admin':

        Loginfrm.destroy()
        from UserInterfaceLayer.MainForm import MainUI
        main_ui = MainUI()
        main_ui.form_load()

    else:
        msg.showerror('Error', 'Your Username or Password is Invalid !')


img_login = PhotoImage(file='UserInterfaceLayer/icon/book-shop.png')
lbl = Label(Loginfrm, image=img_login)
lbl.grid(row=0, column=0, padx=20, pady=10)

txtUserName = StringVar(Loginfrm, value='UserName')
entUserName = Entry(Loginfrm, textvariable=txtUserName, width=40, highlightthickness=1, justify='center')
entUserName.grid(row=1, column=0, padx=20, pady=10)

txtPassword = StringVar(Loginfrm, value='Password')
entPassword = Entry(Loginfrm, textvariable=txtPassword, width=40, highlightthickness=1, show='*', justify='center')
entPassword.grid(row=2, column=0, padx=20, pady=10)


btnLogin = Button(Loginfrm, text='Login', width=33, relief='groove', command=check_login)
btnLogin.grid(row=3, column=0, padx=20, pady=10)

Loginfrm.mainloop()
