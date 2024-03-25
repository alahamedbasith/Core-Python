import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host="localhost",user="root",password="root",database="python_db")

if con:
    print("Connected")
    
    def insert(name, age, city):
        res = con.cursor()
        sql = "insert into users (name,age,city) values (%s,%s,%s)"
        user = (name, age, city)
        res.execute(sql, user)
        con.commit()
        print("Data Insert Success")


    def update(name, age, city,ids):
        res = con.cursor()
        sql = "update users set name=%s,age=%s,city=%s where id=%s"
        user = (name, age, city,ids)
        res.execute(sql, user)
        con.commit()
        print("Data Update Success")



    def display():
        res = con.cursor()
        sql = "SELECT ID,NAME,AGE,CITY from users"
        res.execute(sql)
        # result=res.fetchone()
        # result=res.fetchmany(2)
        result = res.fetchall()
        print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))


    def delete(ids):
        res = con.cursor()
        sql = "delete from users where id=%s"
        user = (ids,)
        res.execute(sql, user)
        con.commit()
        print("Data Delete Success")



    while True:
        print("1.Insert Data")
        print("2.Update Data")
        print("3.Select Data")
        print("4.Delete Data")
        print("5.Exit")
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            name = input("Enter Name : ")
            age = input("Enter Age : ")
            city = input("Enter City : ")
            insert(name, age, city)
        elif choice == 2:
            ids = input("Enter The Id : ")
            name = input("Enter Name : ")
            age = input("Enter Age : ")
            city = input("Enter City : ")
            update(name, age, city,ids)
        elif choice == 3:
            display()
        elif choice == 4:
            ids = input("Enter The Id to Delete : ")
            delete(ids)
        elif choice == 5:
            quit()
        else:
            print("Invalid Selection . Please Try Again !")
else:
    print("OOPS")