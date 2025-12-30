class DBCONNECTIONPYTHON:
    def __init__(self):
        import mysql.connector
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="cybrom"

        )
        self.cursor=self.mydb.cursor()
    def RecordInsert(self,name,age,address,sclass):
        self.name=name
        self.age=age
        self.address=address
        self.sclass=sclass
        sql="insert into python (name,age,address,class) values(%s,%s,%s,%s)"
        value=[self.name,self.age,self.address,self.sclass]
        self.cursor.execute(sql,value)
        self.mydb.commit()
    def RecordDisplay(self):
        sql="select * from python"
        self.cursor.execute(sql)
        mydata=self.cursor.fetchall()
        for i in mydata:
            print(i)
    def RecordUpdate(self):
        name=input("Enter name for update:")
        age=input("Enter age for update:")
        address=input("Enter address for update:")
        sclass=input("Enter the class for update:")
        sql="update python set age=%s,address=%s,class=%s where name=%s"
        value=[age,address,sclass,name]
        self.cursor.execute(sql,value)
        self.mydb.commit()
    def SearchRecord(self):
        name=input("Enter your name:")
        sql="select * from python where name=%s"
        value=[name]
        self.cursor.execute(sql,value)
        mydata=self.cursor.fetchall()
        cnt=self.cursor.rowcount
        if(cnt>=1):
            print(mydata)
        else:
            print("no record found")
    def DeleteRecord(self):
        name=input("Enter your name:")
        sql="delete from python where name=%s"
        value=[name]
        self.cursor.execute(sql,value)
        self.mydb.commit()
        print("record deleted successfully")