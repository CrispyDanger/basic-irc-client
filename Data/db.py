from Data.db_init import Database

def start():
    
    db = Database().connect()
    print("Database initialized", db)
    db.execute("""CREATE TABLE IF NOT EXISTS users(user_id TEXT NOT NULL UNIQUE PRIMARY KEY,
                                                username TEXT NOT NULL, 
                                                password TEXT NOT NULL, 
                                                server_id INTEGER);
                """)
                
    db.execute("""CREATE TABLE IF NOT EXISTS servers(server_id TEXT NOT NULL UNIQUE PRIMARY KEY,
                                                    server TEXT NOT NULL, 
                                                    port INTEGER NOT NULL, 
                                                    channel TEXT NOT NULL,
                                                    user_id INTEGER NOT NULL,
                                                    FOREIGN KEY(user_id) REFERENCES users(user_id)
                                                    ON DELETE CASCADE ON UPDATE CASCADE);""")
    return db 

if __name__ == "__main__":
    start()
