from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/users',methods=['POST'])
def storeuser_DB():
    username = request.form['username']
    password = request.form['password']
    with open("users.txt","w") as userfile:
        userfile.write(username+":"+password)
    return "Successfully Received Database credentials, feel free to visit the http://localhost:5000/schema/dbname or http://localhost:5000/table/dbname/tablename"

@app.route('/schema/<dbname>')
def getschema_DB(dbname):
    str_err = "Username is empty, please use /users endpoint to pass the database username and password first"
    result = "<pre> database: "+dbname+"\n"
    username=""
    password=""
    with open("/home/hkmfsd/PycharmProjects/FP1/users.txt","r") as userfile:
        for line in userfile:
            words = line.split(":")
            username = words[0]
            password = words[1]
    if not bool(username) or not bool(password):
       return str_err
    mydb = mysql.connector.connect(host="localhost", user=username, password=password, database=dbname)
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES")
    tablenames=cursor.fetchall()
    result += "<pre>Table Details"+"\n"
    cursor.close()
    for table_name in tablenames:
        result += "<pre> Table: "+str(table_name).strip("'),(")+"\n"
        cursor1 = mydb.cursor()
        sql = "describe "+str(table_name).strip("'),(")
        cursor1.execute(sql)
        for row in cursor1.fetchall():
            result += "<pre>"+str(row)+"\n"
    return result

@app.route('/table/<dbname>/<tablename>')
def search_table(dbname, tablename):
    str_err = "Username is empty, please use /users endpoint to pass the database username and password first"
    str_notfounferr = "There is no table in the database with name "+str(tablename)
    result = ""
    username=""
    password=""
    with open("/home/hkmfsd/PycharmProjects/FP1/users.txt","r") as userfile:
        for line in userfile:
            words = line.split(":")
            username = words[0]
            password = words[1]
    if not bool(username) or not bool(password):
       return str_err
    mydb = mysql.connector.connect(host="localhost", user=username, password=password, database=dbname)
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES")
    tablenames = cursor.fetchall()
    result += "<pre>Table Details" + "\n"
    cursor.close()
    flag=0
    for table_name in tablenames:
        if (str(table_name).strip("'),(") == tablename):
            flag=1
            result += "<pre> Table: " + str(table_name).strip("'),(") + " found with schema\n"
            cursor1 = mydb.cursor()
            sql = "describe " + str(table_name).strip("'),(")
            cursor1.execute(sql)
            for row in cursor1.fetchall():
                result += "<pre>" + str(row) + "\n"
    if ( flag == 0 ):
        return str_notfounferr
    return result

@app.route('/')
def index():
   return ('<pre> Welcome to database Schema Retrival API '
           '<pre>it has three other endpoints '
           '<pre>1. To provide database credential available at http://localhost:5000 call this from login.html from project folder'
           '<pre>2. To retrive database schema details available at http://localhost:5000/schema/dbname'
           '<pre>3. To search a table in database available at httl://localhost:5000/table/dbname/tablename')

if __name__ == '__main__':
    app.run(debug = True)