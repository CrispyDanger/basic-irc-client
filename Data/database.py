import bcrypt
from data.db_init import DBConnectiom


class Database:
    def __init__(self):
        try:
            self.conn = DBConnectiom().connect()
        except:
            print("Failed")


    def createTable(self):
        create_table_user = """CREATE TABLE IF NOT EXISTS cred(
                    id Integer PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
        );
        """

        create_table_server = """CREATE TABLE IF NOT EXISTS servers(
                                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    server TEXT NOT NULL, 
                                                    port INTEGER NOT NULL, 
                                                    channel TEXT NOT NULL,
                                                    username INTEGER NOT NULL UNIQUE,
                                                    FOREIGN KEY(username) REFERENCES cred(username)
                                                    ON DELETE CASCADE ON UPDATE CASCADE);
                                                    """

        self.conn.execute(create_table_user)
        self.conn.execute(create_table_server)



    def insertData(self, data):

        insert_data = """
        INSERT INTO cred(username, password)
        VALUES(?, ?);
        """
        self.conn.execute(insert_data, data)
        self.conn.execute("COMMIT;")
    
    
    def searchUsers(self, data):
        search_data = """
        SELECT * FROM cred WHERE username = (?);
        """
        self.conn.execute(search_data, data)
        rows = self.conn.fetchall()
        if rows == []:
            return 1
        return 0


    def validateData(self, data, inputData):
        validate_data = """
        SELECT * FROM cred WHERE username = (?);
        """
        
        self.conn.execute(validate_data, data)
        
        row = self.conn.fetchall()
        
        if row[0][1] == inputData[0]:
            return row[0][2] == bcrypt.hashpw(inputData[1].encode(), row[0][2])

    

    def serverList(self, username):
        userdata = (username, )
        data = """
        SELECT server, port, channel FROM servers WHERE username = (?);
        """
        self.conn.execute(data, userdata)
        fetch = self.conn.fetchall()

        return fetch



    def addServer(self,data):
        add_data = """
                INSERT INTO servers(server,port,channel,username) VALUES(?,?,?,?);"""
        self.conn.execute(add_data, data)
        self.conn.execute("COMMIT;")


    def searchServers(self, data):
        search_data = """
        SELECT * FROM servers WHERE server = (?) AND port = (?) AND channel = (?) AND username = (?);
        """
        self.conn.execute(search_data, data)
        rows = self.conn.fetchall()
        if rows == []:
            return 1
        return 0