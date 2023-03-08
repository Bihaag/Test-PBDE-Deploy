from flask import Flask, request, render_template, redirect
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

"""import sqlite3
conn = sqlite3.connect('Login.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT, usertype TEXT)')
conn.commit()
conn.close()"""

"""import sqlite3
conn = sqlite3.connect('Login.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE jobs (JobId INTEGER PRIMARY KEY, Job_Title TEXT, Job_Description TEXT, Faculty TEXT)')
conn.commit()
conn.close()
"""

"""'''sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")'''
sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
'''query1 = "INSERT INTO users (name, password, email, usertype) VALUES(?,?,?)",("Vaish", "123", "vaish@gmail.com", "admin")
cursor.execute(query1)'''
cursor.execute("INSERT INTO users (username, password, email, usertype) VALUES(?,?,?,?)",('Vaish', '123', 'vaish@gmail.com', 'Admin'))
sqlconnection.commit()
sqlconnection.close()"""


"""sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
cursor.execute("INSERT INTO jobs (Job_Title, Job_Description, Faculty) VALUES(?,?,?)",('Data Analyst', 'You will be required to analyse data', 'IT'))
sqlconnection.commit()
sqlconnection.close()"""

'''sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
cursor.execute("DELETE FROM jobs WHERE Job_Title = 'Data Analyst'")
sqlconnection.commit()
sqlconnection.close()'''

'''sqlconnection = sqlite3.connect('Login.db')
cursor = sqlconnection.cursor()
cursor.execute("DELETE FROM users WHERE username = 'Vaish'")
sqlconnection.commit()
sqlconnection.close()'''

myapp = Flask(__name__)


@myapp.route("/")
def homepage():
    return render_template("Homepage.html")

@myapp.route("/", methods = ["POST"])
def checklogin():
    UN = request.form['username']
    PW = request.form['password']
    UT = request.form['usertype']

    '''sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")'''
    sqlconnection = sqlite3.connect('Login.db')
    cursor = sqlconnection.cursor()
    '''query1 = "SELECT Username, Password from users WHERE Username = {un} AND Password = {pw}".format(un = UN, pw = PW)'''

    query1 = "SELECT username, password FROM users WHERE username = ? AND password = ? AND usertype = ?"
    params = (UN, PW, UT)
    
    rows = cursor.execute(query1,params)
    rows = rows.fetchall()
    
    if len(rows) == 1 and UT == "Admin":
        return render_template("LoggedIn.html")
    elif len(rows) == 1 and UT == "Applicant":
        return render_template("LoggedInApplicant.html")
    else:
        '''return redirect("/profilenotfound")'''
        return render_template("ProfileNotFound.html")

@myapp.route("/register", methods = ["GET", "POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form['username']
        dPW = request.form['password']
        Uemail = request.form['email']
        Uusertype = request.form['usertype']
        
        '''sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")'''
        sqlconnection = sqlite3.connect('Login.db')
        cursor = sqlconnection.cursor()
        '''query1 = "INSERT users VALUES('{u}','{p}','{e}')".format(u = dUN, p=dPW, e=Uemail)'''
        query1 = "INSERT INTO users (username, password, email, usertype) VALUES(?, ?, ?, ?)"
        values = (dUN, dPW, Uemail, Uusertype)
        cursor.execute(query1,values)
        sqlconnection.commit()
        '''return redirect("/")'''
        return render_template("SuccessfulRegistration.html")
    return render_template("Register.html")


@myapp.route("/addjob", methods = ["GET", "POST"])
def addjob():
    if request.method == "POST":
        jTitle = request.form['jobtitle']
        jDes = request.form['jobdescription']
        fAc = request.form['faculty']
    

        sqlconnection = sqlite3.connect('Login.db')
        cursor = sqlconnection.cursor()
    
        query1 = "INSERT INTO jobs (Job_Title, Job_Description, Faculty) VALUES(?, ?, ?)"
        values = (jTitle, jDes, fAc)
        cursor.execute(query1,values)
        sqlconnection.commit()
        '''return redirect("/")'''
        return render_template("AddJob.html")
    return render_template("AddJob.html")



if __name__ == "__main__":
   myapp.run(port=8082, debug=True)
