# import sys
# import socket
# import time
# from threading import Thread
# from threading import Event
# import re
# import os
# from datetime import datetime
# import json


# data = json.load(open("config.json"))

# server = data["server"]
# port = data["port"]
# channel = data["channel"]
# botnick = data["botnick"]
# botpassw = data['botpassw']
# log_to_file = data["log_to_file"]


# class IRC_Client:
#     def __init__(self, server, port, channel):
#         pass

#     def send_messages():
#         while True:
#             take = input("~: ")
#             irc.send(f"PRIVMSG {channel} :{take}\r\n".encode())

#     def join():
#         print(f"[/] Connecting to {server}\n")
#         irc.connect((server, port))
#         irc.send(f"USER {botnick} {botnick} {botnick} :This is a fun bot!\r\n".encode())
#         irc.send(f"NICK {botnick}\r\n".encode())
#         irc.send(f"NICKSERV IDENTIFY {botpassw}\r\n".encode())
#         time.sleep(2)

#         irc.send(f"JOIN {channel}\r\n".encode())
#         irc.send(f"PRIVMSG {channel} :`[+] Joined.`\r\n".encode())


#     def read_messages():
#         while True:
#             text = irc.recv(2040)
#             formatted = text.decode()
                
#             if "PRIVMSG" in formatted:
#                 arr = re.split("!~.*\s+PRIVMSG\s+|\s+:", formatted[1:], maxsplit=2)
#                 user_messages = f"<{arr[0]}> {arr[-1]}"
#                 now = datetime.now()
#                 get_current_time = now.strftime("%H:%M:%S")
#                 print("\n" + get_current_time + " | " + user_messages, end = "")
#                 if log_to_file == "true":
#                     f = open("logs.txt", "a", encoding="utf-8")
#                     f.write("\n" + get_current_time + " | " + user_messages)
#                     f.close()

#             if "PING" in formatted:
#                 encoded = ('PONG ' + formatted.split()[1]).encode()
#                 print(encoded)
#                 irc.send(encoded)

# try:
#     irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     event = Event()
#     event.set()
#     IRC_Client.join()

#     Thread(target = IRC_Client.read_messages).start()
#     Thread(target = IRC_Client.send_messages).start()

# except KeyboardInterrupt:
#     print("[+] Exiting...")
#     irc.send(f"PRIVMSG {channel} :`[+] Exiting...`\r\n".encode())
