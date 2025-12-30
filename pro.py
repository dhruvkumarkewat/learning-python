import pro1
ob1=pro1.DBCONNECTIONPYTHON()
while(True):
    print("""
    press 1 for insert
    press 2 for display
    press 3 for update
    press 4 find data using name
    press 5 for delete
    press 6 for exit
""")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        print("insert")
        name=input("Enter your name:")
        age=input("Enter your age:")
        address=input("Enter your address:")
        sclass=input("Enter your class:")
        ob1.RecordInsert(name,age,address,sclass)
        print("inserted succesfully")
    elif(ch==2):
        print("display")
        ob1.RecordDisplay()
    elif(ch==3):
        print("update")
        ob1.RecordUpdate()
    elif(ch==4):
        ob1.SearchRecord()
        print("record find successfully")
    elif(ch==5):
        ob1.DeleteRecord()
    elif(ch==6):
        print("exit")
        break
    else:
        print("wrong choice")
    
