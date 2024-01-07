import mysql.connector

mydb=mysql.connector.connect(
     host="localhost",
     user="root",
    password="",
    database="suresh_app_node3"
    
) 
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE SAMPLE (id  INT,name VARCHAR(200))")
#sql="INSERT INTO SAMPLE (id,name) VALUES (%s,%s)"
#val=("1","Suresh")
#mycursor.execute(sql,val)
#mydb.commit()
#print(mycursor.rowcount,"record inserted.")#
mycursor.execute("SELECT *FROM SAMPLE ")

myresult=mycursor.fetchall()

for x in myresult:
  print(x)  
