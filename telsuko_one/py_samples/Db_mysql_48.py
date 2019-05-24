import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="pydb")
mycursor = mydb.cursor()

mycursor.execute("select * from py_student")

#for i in mycursor:
#    print(i)

#results = mycursor.fetchall()
#for i in results:
#    print(i)

for i in mycursor.fetchmany(2):
    print(i)