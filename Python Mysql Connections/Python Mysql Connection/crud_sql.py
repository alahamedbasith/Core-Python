import sqlite3 as sql

# Use a raw string to avoid Unicode escape error
connection = sql.connect(r'D:\Python Projects\Python Mysql Connection\users.db')


def insert_data(name, age, city):
    query = "INSERT INTO users(NAME, AGE, CITY) VALUES (?, ?, ?);"
    connection.execute(query, (name, age, city))
    connection.commit()
    print("The user details added successfully")
    
def update_data(ids,name,age,city):
    query = "UPDATE users SET NAME=?, AGE=?, CITY=? WHERE ID=?;"
    connection.execute(query, (name, age, city,ids))
    connection.commit()
    print("The user details updated successfully")
    
def delete_data(ids):
    query = "DELETE from users WHERE ID=?;"
    connection.execute(query, (ids,)) # See this is tuple object so i was add comma otherwise error occurs
    connection.commit()
    print("The user details deleted successfully")

def display_data():
    query = "SELECT * FROM users;"
    result = connection.execute(query)
    for row in result:
        print(row)
    

print("""
      1. INSERT
      2. UPDATE
      3. DELETE
      4. DISPLAY
      5. PRESS ANY KEY TO EXIT
      """)

while True:
    ch = int(input("Enter the choice:"))

    if ch == 1:
        print("Add new record")
        name = input("Enter the name:")
        age = int(input("Enter the age:"))
        city = input("Enter the city:")
        insert_data(name, age, city)
        
    elif ch == 2:
        print("Update or Edit a record")
        ids = int(input("Enter the user ID:"))
        name = input("Enter the name:")
        age = int(input("Enter the age:"))
        city = input("Enter the city:")
        update_data(ids,name, age, city)
        
    elif ch == 3:
        print("Delete a record")
        ids = int(input("Enter the user ID:"))
        delete_data(ids)
        
    elif ch == 4:
        print("Display all records")
        display_data()
    else:
        connection.close()  # Close the connection before exiting the program
        break
