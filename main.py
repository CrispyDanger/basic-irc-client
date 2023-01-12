import Data.db as database
from irc import IRC_Client
from uuid import uuid4

db = database.start()


def get_uuid():
    return uuid4().hex


def main():
    print("Would you like to login? [Y/N] \n")
    inp = input()
    if inp == "Y":
        print("Please enter your login and password in this format <username:password>: \n")
        login = input().split(":")
        username = login[0]
        password = login[1]
        res = db.execute(f"""SELECT username FROM users WHERE username == {username} AND password == {password} """)
        if res:
            print("User Found!")
        else:
            print("User not Found!")


if __name__ == "__main__":
    main()






