import sqlite3

def read_all(database):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("SELECT * FROM users;")
        results = c.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e: 
        print(f"Failed to retrieve accounts: {e} ")


def read(database, username):
    try: 
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username =?;", [username])
        results = c.fetchone()
        conn.close()
        return results

    except sqlite3.Error as e:
        print(f"Failed to retrieve account: {e}")

def create(database, username, password):
    try: 
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?,?)", [username, password])
        conn.commit()
        conn.close()

        return results
    except sqlite3.Error as e:
        print(f"Failed to create account")



def delete(database, account_id):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id =?", [account_id])
        conn.commit()
        conn.close()


    except sqlite3.Error as e:
        print(f"Failed to delete username")