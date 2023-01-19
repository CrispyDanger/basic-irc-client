from tkinter import Tk,Label,Button
from windows import Login, Register,Servers



class MainWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("Login")
        self.app.geometry("300x250")
        self.label = Label(self.app, text="Welcome To App")
        self.label.place(x=95, y=40)
        self.login = Button(self.app, text="Login",
                            pady=5, padx=30, command=self.login_fnc)
        self.login.place(x=100, y=100)
        self.register = Button(self.app, text="Register",
                               pady=5, padx=20, command=self.register_fnc)
        self.register.place(x=100, y=150)
        self.register = Button(self.app, text="Servers",
                               pady=5, padx=20, command=self.server_list_fnc)
        self.register.place(x=100, y=200)


    def run(self):
        self.app.mainloop()



    def login_fnc(self):
        loginTk = Login()
        loginTk.run()



    def register_fnc(self):
        registerTk = Register()
        registerTk.run()



    def server_list_fnc(self):
        serverTk = Servers()
        serverTk.run



app = MainWindow()
app.run()