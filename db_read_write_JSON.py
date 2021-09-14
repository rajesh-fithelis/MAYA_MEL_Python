import mysql.connector
import json
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
def dataInsert():
   print("inside insert done")
   mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
    )
   mycursor = mydb.cursor()
   sql = "INSERT INTO projectDB.projects (projectName, status) VALUES (%s, %s)"
   val = [
   ('ICE', 'published'),
   ('IC2', 'in-progress'),
   ('NXP', 'pending'),
   ('PPX', 'client approved'),
   ('AAU', 'internal approved'),
   ('POP', 'in-review'),
   ('CCB', 'pending'),
   ('EWU', 'internal approved'),
   ('WWP', 'in-review'),
   ('CSB', 'pending')
   ]
   mycursor.executemany(sql, val)
   mydb.commit()
   print(mycursor.rowcount, "was inserted.")
   print("data insert done")

def dbCreate():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
  )
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE IF NOT EXISTS projectDB;")
  ProjectTableSql = "CREATE TABLE IF NOT EXISTS projectDB.projects(projectsKey INT(20) PRIMARY KEY AUTO_INCREMENT, projectName  VARCHAR(100) NOT NULL, status VARCHAR(100) NOT NULL);"
  mycursor.execute(ProjectTableSql)
  mydb.close()
  print("creat prj done")


def createJSON():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
  )
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM projectDB.projects ORDER BY status;")
  records = mycursor.fetchall()
  newJSONDATA ={}
  data = {}
  tmp = {}
  i=0
  for row in records:
     print(row[1])
     tmp["projectsKey"] = row[0]
     tmp["projectName"] = row[1]
     tmp["status"] = row[2]
     data[i] = tmp
     i += 1

  newJSONDATA["projectDB"]=data
  with open('projectDB_SPARKY_data.json', 'w') as outfile:
     json.dump(newJSONDATA, outfile)

 

if __name__ == '__main__':
    dbCreate()
    dataInsert()
    createJSON()