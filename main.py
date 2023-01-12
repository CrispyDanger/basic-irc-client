import Data.db as database
# from irc import IRC_Client
from uuid import uuid4
import bcrypt
import getpass 


db = database.start()


def get_uuid():
    return uuid4().hex


def main():
    print("Would you like to login? [y/n]")
    inp = input()
    if inp == "y":
        login()
    if inp == "n":
        print("Do you want to register? [y/n]")
        inp2 = input()
        if inp2 == "y":
            register()



def login():
    print("Please enter your login and password in this format <username:password>:")
    login = input().split(":")
    username = login[0]
    password = login[1]

    statement = (f"""SELECT username FROM users WHERE username='{username}' AND password = '{password}' """)
    db.execute(statement)

    if not db.fetchone():
        print("User not Found!")
        print("Do you want to register? [y/n]")
        reg = input()
        if reg == "y":
            register()
    else:
        print("User Found!")


def register():
    print("Please enter your username:")
    username = input()
    find_username = (f"""SELECT username FROM users WHERE username='{username}';""")
    db.execute(find_username)
    if db.fetchone():
        print("This user name was taken! Choouse another one")
    else:
        print("Please enter your password")
        password = getpass.getpass(prompt="Password:").encode()
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)
        user = (get_uuid(), username, hashed_password)
        statement = (f"""INSERT Into users(user_id, username, password) VALUES(?,?,?);""")
        db.execute(statement, user)
        db.execute("COMMIT;")









if __name__ == "__main__":
    main()






