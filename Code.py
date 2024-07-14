import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="root",database="LIBRARY")
def addbook():
    bn=input("enter BOOK name:")
    c=input("enter BOOK code:")
    t=input("Total Books:")
    s=input("Enter Genre:")
    data=(bn,c,t,s)
    sql="insert into books values (%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("-------data entered successfully-------")
    main()
def issueb():
    n=input("Enter name:")
    r=input("enter reg no:")
    co=input("enter book code:")
    d=input("enter date:")
    data=(n,r,co,d)
    a="insert into issue values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("book issued to:",n)
    bookup(co,-1)
def submitb():
    n=input("Enter name:")
    r=input("enter reg no:")
    co=input("enter book code:")
    d=input("enter date:")
    data=(n,r,co,d)
    a="insert into submit values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("book submitted from:",n)
    bookup(co,1)
def bookup(co,u):
    a="select TOTAL from books where BCODE=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL=%s where BCODE=%s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()
def dbook():
    ac=input("enter book code:")
    a="delete from books where BCODE=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()
def dispbook():
    a="select* from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name:",i[0])
        print("Book COde:",i[1])
        print("Total:",i[2])
        print(">---------------------------<")
    main()
def main():
    print("""
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.DISPLAY BOOKS
    """)
    choice=input("Enter task no.")
    if (choice=='1'):
        addbook()
    elif (choice=='2'):
        issueb()
    elif (choice=='3'):
        submitb()
    elif (choice=='4'):
        dbook()
    elif (choice=='5'):
        dispbook()
    else:
        print("Wrong choice")
        main()
def pswd():
    ps=input("enter password:")
    if ps=="1234":
        main()
    else:
        print("wrong password")
        pswd()
pswd()