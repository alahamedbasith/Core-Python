import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)  # Establish Connection
        self.cur = self.con.cursor()
        
        sql = """
        
         CREATE TABLE IF NOT EXISTS employees(
             id integer Primary Key,
             name text,
             age text,
             doj text,
             email text,
             gender text,
             contact text,
             address text
        
             )
        
        """
        
        self.cur.execute(sql)
        self.con.commit()
        
    # Insert function
    def insert(self,name,age,doj,email,gender,contact,address):
            
        sql = "insert into employees values (NULL,?,?,?,?,?,?,?)"
        val = (name,age,doj,email,gender,contact,address)
        self.cur.execute(sql,val)
        self.con.commit()
        
    # Update function
    def update(self,id,name,age,doj,email,gender,contact,address):
        sql = "update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?"
        val = (name,age,doj,email,gender,contact,address,id)
        self.cur.execute(sql,val)
        self.con.commit()


    # Fetch all data from database
    def fetch(self):
        self.cur.execute("select * from employees")
        result = self.cur.fetchall()
        print(result)
        return result
        
    # Delete a data from database
    def delete(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()

# obj = Database("Employee.db")
# obj.insert("Najim","21,24-2-2024","ahamed@gmail.com","male","9087654321","Pallivasal street")
# obj.delete(2)
# obj.update(5,"yousuf",21,"24-2-2024","yousuf@gmail.com","male","9087654321","Pallivasal street")
# obj.fetch()
