from tkinter import *
from tkinter import messagebox
from windows import Register,Servers
from database import Database




class MainWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("Login")
        self.app.geometry("300x250")
        self.db = Database()
        self.label = Label(self.app, text="Welcome To App")
        self.label.place(x=95, y=40)


        self.label = Label(self.app, text="Login")
        self.label.place(x=90, y=60)
        

        self.username_entry = Entry(
        self.app, relief=FLAT)
        self.username_entry.place(x=90, y=80)
        self.password_entry = Entry(
        self.app, show="*", relief=FLAT)
        self.password_entry.place(x=90, y=120)
        
        
        self.submit = Button(self.app, text="Login",
        pady=5, padx=20, command=self.validate)
        self.submit.place(x=150, y=150)
        self.register = Button(self.app, text="Register",
                               pady=5, padx=20, command=self.register_fnc)
        self.register.place(x=50, y=150)


    def run(self):
        self.app.mainloop()


    def validate(self):
       self.username = self.username_entry.get()
       self.password = self.password_entry.get()
       data = (self.username,)
       inputData = (self.username, self.password,)
       
       try:
           if (self.db.validateData(data, inputData)):
               messagebox.showinfo("Successful", "Login Was Successful")
               self.server_list_fnc(self.username)
           else:
               messagebox.showerror("Error", "Wrong Credentials")
       except IndexError:
           messagebox.showerror("Error", "Wrong Credentials")   



    def register_fnc(self):
        registerTk = Register()
        registerTk.run()



    def server_list_fnc(self,username):
        serverTk = Servers(username)
        serverTk.run



app = MainWindow()
app.run()