from tkinter import *
from tkinter import messagebox
import bcrypt
from data.database import Database
import irc
import threading

db = Database()


class Register:

    def __init__(self):
        self.registerWindow = Tk()
        self.registerWindow.title("Register with Python")
        self.registerWindow.geometry("300x250")
        self.label = Label(self.registerWindow, text="Register")
        self.label.place(x=95, y=40)
        
        self.username_entry = Entry(self.registerWindow, relief=FLAT)
        self.username_entry.place(x=70, y=80)
        self.password_entry = Entry(self.registerWindow, show="*", relief=FLAT)
        self.password_entry.place(x=70, y=120)
        self.submit = Button(self.registerWindow,
        text="Submit", pady=5, padx=20, command=self.add)
        self.submit.place(x=100, y=150)
        
        
    def run(self):
        self.registerWindow.mainloop()



    def add(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.salt = bcrypt.gensalt()
        self.hashed = bcrypt.hashpw(self.password.encode(), self.salt)
        data = (self.username,)
        result = db.searchUsers(data)
        if result != 0:
            data = (self.username, self.hashed)
            db.insertData(data)
            messagebox.showinfo("Successful", "Username Was Added")
        else:
            messagebox.showwarning("Warning", "Username already Exists")



class Servers:

    def __init__(self, username):
        self.serverListWindow = Toplevel()
        self.serverListWindow.title("Server_List")
        self.serverListWindow.geometry("400x250")
        self.username = username

        self.label = Label(self.serverListWindow, text="Server Address:")
        self.label.place(x=200, y=20)

        self.server_entry = Entry(self.serverListWindow, relief=FLAT)
        self.server_entry.place(x=200, y=40)

        self.label = Label(self.serverListWindow, text="Port:")
        self.label.place(x=200, y=60)

        self.port_entry = Entry(self.serverListWindow, relief=FLAT)
        self.port_entry.place(x=200, y=80)

        self.label = Label(self.serverListWindow, text="Channel:")
        self.label.place(x=200, y=100)

        self.channel_entry = Entry(self.serverListWindow, relief=FLAT)
        self.channel_entry.place(x=200, y=120)

        self.submit = Button(self.serverListWindow,
        text="Add", pady=5, padx=20, command=self.add)
        self.submit.place(x=200, y=140)


        lst = db.serverList(self.username)

        server_list = [server for server in lst]
        self.servers_var = Variable(value=server_list)
        self.selection_label = Label()

        self.listbox = Listbox(self.serverListWindow, selectmode=SINGLE)
        self.listbox.place(x=50, y=50)

        for server in server_list:  
            self.listbox.insert(0, server)


        self.submit = Button(self.serverListWindow,
        text="Connect", pady=5, padx=20, command=threading.Thread(target=self.connect, daemon=True).start)
        self.submit.place(x=200, y=200)



    def run(self):
        self.serverListWindow.mainloop()


    def connect(self):
        resp = False
        while resp is False:
            server = self.listbox.curselection()[0]
            resp = irc.main(self.listbox.get(server), self.username)



    def add(self):
        self.server = self.server_entry.get()
        self.port = self.port_entry.get()
        if self.port.isdigit() and len(self.port) == 4:
            self.channel = self.channel_entry.get()
            if self.channel.startswith("#"):
                pass
            else:
                self.channel = "#" + self.channel
            data = (self.server,self.port,self.channel, self.username)
            result = db.searchServers(data)
            if result:
                db.addServer(data)
                self.listbox.insert(0, str(data[:3]))
            else:
                messagebox.showwarning("Warning", "Server already in the list")
        else:
            messagebox.showwarning("Warning", "Port is not a number or exceeds 4 symbol limit")

        
        
        
        
 

 

 
