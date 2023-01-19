import sqlite3
import bcrypt



class Database:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("test.db")
            print("Successfully Opened Database")
            self.curr = self.conn.cursor()
        except:
            print("Failed")


    def createTable(self):
        create_table_user = """CREATE TABLE IF NOT EXISTS cred(
                    id Integer PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        );
        """

        create_table_server = """CREATE TABLE IF NOT EXISTS servers(
                                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    server TEXT NOT NULL, 
                                                    port INTEGER NOT NULL, 
                                                    channel TEXT NOT NULL,
                                                    username INTEGER NOT NULL,
                                                    FOREIGN KEY(username) REFERENCES cred(username)
                                                    ON DELETE CASCADE ON UPDATE CASCADE);"""

        self.curr.execute(create_table_user)
        self.curr.execute(create_table_server)
        self.conn.commit()


    def insertData(self, data):

        insert_data = """
        INSERT INTO cred(username, password)
        VALUES(?, ?);
        """
        self.curr.execute(insert_data, data)
        self.conn.commit()
    
    
    def searchUsers(self, data):
        search_data = """
        SELECT * FROM cred WHERE username = (?);
        """
        self.curr.execute(search_data, data)
        rows = self.curr.fetchall()
        if rows == []:
            return 1
        return 0


    def validateData(self, data, inputData):
        print(data)
        print(inputData)
        validate_data = """
        SELECT * FROM cred WHERE username = (?);
        """
        
        self.curr.execute(validate_data, data)
        
        row = self.curr.fetchall()
        
        if row[0][1] == inputData[0]:
            return row[0][2] == bcrypt.hashpw(inputData[1].encode(), row[0][2])

    

    def serverList(self):
        data = """
        SELECT server, port, channel FROM servers;
        """
        self.curr.execute(data)
        fetch = self.curr.fetchall()
        print(fetch)

        return fetch



    def addServer(self,data):
        add_data = """
                INSERT INTO servers(server,port,channel,username) VALUES(?,?,?,?);"""
        self.curr.execute(add_data, data)
        self.conn.commit()


    def searchServers(self, data):
        search_data = """
        SELECT * FROM servers WHERE server = (?) AND port = (?) AND channel = (?);
        """
        self.curr.execute(search_data, data)
        rows = self.curr.fetchall()
        if rows == []:
            return 1
        return 0