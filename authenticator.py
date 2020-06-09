import sqlite3

conn = sqlite3.connect("user_database.db")


c = conn.cursor()

def authenticate(username, password):
    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()
    
    c.execute("SELECT oid, * FROM users")
    var = c.fetchall()
    for record in var:
        if((record[2] == username) & (record[3] == password)):
            conn.commit()
            conn.close()
            return True
    
    conn.commit()
    conn.close()
    return False


def add_user(name, username, password, address, number, email):
    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()
    
    # Insert into Table
    c.execute("INSERT INTO users VALUES (:name,:username,:password,:address,:number,:email)",{
            'name':name,
            'username':username,
            'password':password,
            'address':address,
            'number':number,
            'email': email
        })
        
    conn.commit()
    conn.close()
    return True
    
# commit to databases
conn.commit()

# Close the Connection
conn.close()

