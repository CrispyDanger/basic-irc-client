import sys
import socket
import time
from threading import Thread
from threading import Event
import re
import os
from datetime import datetime

class IRCClient:
    def __init__(self, server,username, log_to_file=True):
        self.server = server[0]
        self.port = server[1]
        self.channel = server[2]
        self.username = username
        self.passw = ""
        self.log_to_file = log_to_file
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        


    def send_messages(self):
        while True:
            take = input("~: ")
            if take == "?EXIT" or take == "~: ?EXIT":
                self.stop()
            self.irc.send(f"PRIVMSG {self.channel} :{take}\r\n".encode())

    def connect(self):
        print(f"[/] Connecting to {self.server}\n")
        self.irc.connect((self.server, self.port))
        self.irc.send(f"USER {self.username} {self.username} {self.username} :Hello, everyone!\r\n".encode())
        self.irc.send(f"NICK {self.username}\r\n".encode())
        self.irc.send(f"NICKSERV IDENTIFY {self.passw}\r\n".encode())
        time.sleep(2)

        self.irc.send(f"JOIN {self.channel}\r\n".encode())



    def read_messages(self):
        while True:
            text = self.irc.recv(2040)
            formatted = text.decode()
                
            if "PRIVMSG" in formatted:
                arr = re.split("!~.*\s+PRIVMSG\s+|\s+:", formatted[1:], maxsplit=2)
                user_messages = f"<{arr[0]}> {arr[-1]}"
                now = datetime.now()
                get_current_time = now.strftime("%H:%M:%S")
                print("\n" + get_current_time + " | " + user_messages, end = "")
                if self.log_to_file == "true":
                    f = open("logs.txt", "a", encoding="utf-8")
                    f.write("\n" + get_current_time + " | " + user_messages)
                    f.close()

            if "PING" in formatted:
                encoded = ('PONG ' + formatted.split()[1]).encode()
                print(f"Successfully connected to {self.channel}")
                self.irc.send(encoded)

    
    def run(self):
        while True:
            self.event = Event()
            self.connect()
            self.t1 = Thread(target = self.read_messages)
            self.t2 = Thread(target = self.send_messages)
            self.t2.daemon = True
            self.t1.start()
            self.t2.start()
            self.t1.join()
            self.t2.join()
            if self.event.is_set():
                exit()
    

    def stop(self):
        self.event.set()
        print("[+] Exiting...")
        exit()



def main(server, username):
    irc = IRCClient(server, username)
    irc.run()
