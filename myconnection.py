import mysql.connector
mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="cybrom"
)
mycursor=mydb.cursor()
name=input("enter your name:")
age=input("Enter your age:")
address=input("Enter your address:")
sclass=input("Enter your class:")
sql="insert into python (name,age,address,class) values(%s,%s,%s,%s) "
value=[name,age,address,sclass]
mycursor.execute(sql,value)
mydb.commit()
print("inserted")