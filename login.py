from tkinter import *
from tkinter import messagebox
import bcrypt
from database import Database
db = Database()
db.createTable()
class Login:
    def __init__(self):
        self.loginWindow = Tk()
        self.loginWindow.title("Login with Python")
        self.loginWindow.geometry("300x250")
        self.label = Label(self.loginWindow, text="Login")
        self.label.place(x=95, y=40)
        # Just Creepy Tkinter Stuff
        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.usernameE = Entry(
        self.loginWindow, relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=70, y=80)
        self.passwordE = Entry(
        self.loginWindow, show="*", relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=70, y=120)
        # Actual Variales
        self.username = self.usernameS.get()
        self.password = self.passwordS.get()
        self.submit = Button(self.loginWindow, text="Submit",
        pady=5, padx=20, command=self.validate)
        self.submit.place(x=100, y=150)


    def validate(self):
        data = (self.username,)
        inputData = (self.username, self.password,)
        try:
            if (db.validateData(data, inputData)):
                messagebox.showinfo("Successful", "Login Was Successful")
            else:
                messagebox.showerror("Error", "Wrong Credentials")
        except IndexError:
            messagebox.showerror("Error", "Wrong Credentials")


    def run(self):
        self.loginWindow.mainloop()


class Register:

    def __init__(self):
        self.registerWindow = Tk()
        self.registerWindow.title("Register with Python")
        self.registerWindow.geometry("300x250")
        self.label = Label(self.registerWindow, text="Register")
        self.label.place(x=95, y=40)
        # Just Creepy Tkinter Stuff
        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.usernameE = Entry(self.registerWindow,
        relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=70, y=80)
        self.passwordE = Entry(self.registerWindow, show="*",
        relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=70, y=120)
        self.submit = Button(self.registerWindow,
        text="Submit", pady=5, padx=20, command=self.add)
        self.submit.place(x=100, y=150)
        # Actual Variales
        self.username = self.usernameS.get()
        self.password = self.passwordS.get()
        self.salt = bcrypt.gensalt()
        self.hashed = bcrypt.hashpw(self.password.encode(), self.salt)
    
    
    def run(self):
        self.registerWindow.mainloop()


    def add(self):
        data = (self.username,)
        result = db.searchData(data)
        print(result)
        if result != 0:
            data = (self.username, self.hashed)
            db.insertData(data)
            messagebox.showinfo("Successful", "Username Was Added")
        else:
            messagebox.showwarning("Warning", "Username already Exists")