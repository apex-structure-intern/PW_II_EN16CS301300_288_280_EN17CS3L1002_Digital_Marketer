import sqlite3

conn = sqlite3.connect("user_database.db")


c = conn.cursor()

def query():
    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()
    
    c.execute("SELECT oid, * FROM users")
    var = c.fetchall()
    print(var)
    
    conn.commit()
    conn.close()


def submit(name, username, password, address, number, email):
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
    
#submit('Yuvraj','admin','admin','nullified','8962209349','gui@gmail.com')
query()
# commit to databases
conn.commit()

# Close the Connection
conn.close()

