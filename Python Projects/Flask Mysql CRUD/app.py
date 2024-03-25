from flask import Flask, render_template, flash, redirect, url_for, request, get_flashed_messages
import mysql.connector

app = Flask(__name__)

# Connect to MySQL using mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="root", database="python_flask_db")

if con:
    print("Connected to MySQL successfully!")

@app.route("/")
def home():
    try:
        # Create cursor
        cur = con.cursor(dictionary=True)

        # Execute query
        cur.execute("SELECT * FROM users")

        # Fetch data
        data = cur.fetchall()

        # Close cursor
        cur.close()

        # Render template with data
        return render_template('confirm.html', data=data)
    except mysql.connector.Error as e:
        return f"Error connecting to MySQL: {e}"

# New User
@app.route("/addUsers", methods=['GET', 'POST'])
def addUsers():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        
        try:
            # Create cursor
            cur = con.cursor()

            # Execute query
            sql = "INSERT INTO users (NAME, CITY, AGE) VALUES (%s, %s, %s)"
            val = (name, city, age)
            cur.execute(sql, val)

            # Commit changes
            con.commit()

            # Close cursor
            cur.close()
            
            flash("User details added successfully")

            return redirect(url_for("home")) # Back to homepage
        
        except mysql.connector.Error as e:
            return f"Error inserting data into MySQL: {e}"
    
    return render_template("addusers.html")

# Update User
@app.route("/editUser/<string:id>",methods=['GET','POST'])
def editUser(id):
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        
        try:
            # Create cursor
            cur = con.cursor()
        
            sql = "update users set NAME=%s,CITY=%s,AGE=%s where ID=%s"
            val = (name,city,age,id)
            cur.execute(sql,val)
            
            # Commit Changes
            con.commit()
            
            # Close cursor
            cur.close()
            
            flash("User details updated successfully")
            
            return redirect(url_for("home"))
        
        except mysql.connector.Error as e:
            return f"Error inserting data into MySQL: {e}"
        
    # Create cursor
    cur = con.cursor(dictionary=True)
    
    sql = "select * from users where ID=%s"
    val = (id,)
    cur.execute(sql,val)
    
    result = cur.fetchone()
    
    if result:
        return render_template("edituser.html", data=result)
    else:
        return "User not found" 
    
# Delete User
@app.route("/deleteUser/<string:id>",methods=['GET','POST'])
def deleteUser(id):
    try:
        # Create cursor
        cur = con.cursor()
    
        sql = "delete from users where ID=%s"
        val = (id,)
        cur.execute(sql,val)
        
        # Commit Changes
        con.commit()
        
        # Close cursor
        cur.close()
        
        flash("User details deleted successfully")
        
        return redirect(url_for("home"))
    
    except mysql.connector.Error as e:
        return f"Error inserting data into MySQL: {e}"
    
        

if __name__ == '__main__':
    # Flash needs secret key
    app.secret_key = "123456"
    app.run(debug=True)
