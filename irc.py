import sys
import socket
import time
from threading import Thread
from threading import Event
import re
import os
from datetime import datetime
from main import MainWindow


# def threaded(fnc):
#         def wrapper(*args, **kwargs):
#             thread = Thread(target=fnc)
#             thread.start
#             return thread
#         return wrapper



# class IRCClient:
#     def __init__(self, server,username, log_to_file=True):
#         self.server = server[0]
#         self.port = server[1]
#         self.channel = server[2]
#         self.username = username
#         self.passw = ""
#         self.log_to_file = log_to_file
#         self.event = Event()
#         self.event.set()
#         self.join()

#         Thread(target = self.read_messages).start()
#         Thread(target = self.send_messages).start()
                

#     @threaded
#     def send_messages(self):
#         while True:
#             take = input("~: ")
#             self.irc.send(f"PRIVMSG {self.channel} :{take}\r\n".encode())

#     def join(self):
#         self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         print(f"[/] Connecting to {self.server}\n")
#         self.irc.connect((self.server, self.port))
#         self.irc.send(f"USER {self.username} {self.username} {self.username} :Hello, everyone!\r\n".encode())
#         self.irc.send(f"NICK {self.username}\r\n".encode())
#         self.irc.send(f"NICKSERV IDENTIFY {self.passw}\r\n".encode())
#         time.sleep(2)

#         self.irc.send(f"JOIN {self.channel}\r\n".encode())
#         self.irc.send(f"PRIVMSG {self.channel} :`[+] Joined.`\r\n".encode())

#     @threaded
#     def read_messages(self):
#         while True:
#             text = self.irc.recv(2040)
#             formatted = text.decode()
                
#             if "PRIVMSG" in formatted:
#                 arr = re.split("!~.*\s+PRIVMSG\s+|\s+:", formatted[1:], maxsplit=2)
#                 user_messages = f"<{arr[0]}> {arr[-1]}"
#                 now = datetime.now()
#                 get_current_time = now.strftime("%H:%M:%S")
#                 print("\n" + get_current_time + " | " + user_messages, end = "")
#                 if self.log_to_file == "true":
#                     f = open("logs.txt", "a", encoding="utf-8")
#                     f.write("\n" + get_current_time + " | " + user_messages)
#                     f.close()

#             if "PING" in formatted:
#                 encoded = ('PONG ' + formatted.split()[1]).encode()
#                 print(encoded)
#                 self.irc.send(encoded)

    


def send_messages():
    while True:
        take = input("~: ")
        irc.send(f"PRIVMSG {channel} :{take}\r\n".encode())

def join():
    print(f"[/] Connecting to {server}\n")
    irc.connect((server, port))
    irc.send(f"USER {username} {username} {username} :Testing!\r\n".encode())
    irc.send(f"NICK {username}\r\n".encode())
    irc.send(f"NICKSERV IDENTIFY {passw}\r\n".encode())
    time.sleep(2)

    irc.send(f"JOIN {channel}\r\n".encode())
    irc.send(f"PRIVMSG {channel} :`[+] Joined.`\r\n".encode())


def read_messages():
    while True:
        text = irc.recv(2040)
        formatted = text.decode()

        if "PRIVMSG" in formatted:
            arr = re.split("!~.*\s+PRIVMSG\s+|\s+:", formatted[1:], maxsplit=2)
            user_messages = f"<{arr[0]}> {arr[-1]}"
            now = datetime.now()
            get_current_time = now.strftime("%H:%M:%S")
            print("\n" + get_current_time + " | " + user_messages, end = "")
            if log_to_file == "true":
                f = open("logs.txt", "a", encoding="utf-8")
                f.write("\n" + get_current_time + " | " + user_messages)
                f.close()

        if "PING" in formatted:
            encoded = ('PONG ' + formatted.split()[1]).encode()
            print(encoded)
            irc.send(encoded)


try:
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mainWidnow = MainWindow()
    mainWidnow.run()

    server, port, channel, username = mainWidnow.connect()


    passw = ""
    log_to_file = True


    event = Event()
    event.set()
    join()

    Thread(target = read_messages).start()
    Thread(target = send_messages).start()

except KeyboardInterrupt:
    print("[+] Exiting...")
    irc.send(f"PRIVMSG {channel} :`[+] Exiting...`\r\n".encode())