import mysql.connector
import re
import random


con = mysql.connector.connect(host="localhost", password="Tiger", user="Student", database="abc")


def psd():
    global run
    global phno
    global tr
    tr = ""
    for i in range(3):
        run = input("Enter password to access program: ")
        if run == "123":
            print("\n--Welcome to our program!!--")
            tr = 0
            i = i + 1
            break
        else:
            print("You have entered incorrect password!!")


def mainps():
    global hi
    hi = "tigerr"
    emp = input("Enter employee password:")
    if emp == hi:
        print("WELCOME!")
    else:
        print("WRONG PASSWORD!!")


def openingAccount():
    name = input("Enter Account holder's name: ")

    accno = int(''.join([str(random.randint(0, 10)) for _ in range(12)]))

    print("Your account number is: ", accno)

    dob = input("Enter D.O.B (YYYY-MM-DD): ")
    year, month, date = dob.split('-')
    date = int(date)
    month = int(month)
    year = int(year)
    if month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_days = 31
    elif month == 4 or month == 9 or month == 11:
        max_days = 30
    elif year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        max_days = 29
    else:
        max_days = 28
    if month < 1 or month > 12:
        print("check the range of month")
        while 0 == False:
            dt = input("Enter date:")
            break
    elif date < 1 or date > max_days:
        print("check the range of date")
        while 0 == False:
            d = input("Enter date:")
            break
    elif year < 1922 or year > 2022:
        print("check the range of year")
        while 0 == False:
            d = input("Enter date:")
            break
    else:
        print()

    for i in range(0, 4):
        phno = input("Enter Phone no.: ")
        pattern = re.compile("(0|91)?[-\s]?[6-9][0-9]{9}")
        if pattern.match(phno):
            print()
            break
        else:
            print(f"{phno} is not valid.")
            i = i + 1
            continue

    ad = input("Enter Address: ")

    adhr = input("Enter Aadhar card number: ")
    if len(adhr) == 12:
        print()
    else:
        print("check the range of aadhar no")
        while 0 == False:
            ad = input("Enter aadhar no:")
            break

    gender = input("Enter Gender (M/F/O): ")

    fn = input("Enter Father's name: ")

    mn = input("Enter Mother's name: ")

    ob = int(input("Enter Opening Balance: "))

    global us
    global pas

    us = input("enter username: ")
    print("Your username is:", us)

    ps = input("Enter password - \n (Enter 6 character alphanumeric password):  ")
    print("Your password is: ", ps)

    data1 = (name, accno, dob, ob, us, adhr, fn, mn, phno, gender, ad, ps)
    data2 = (name, accno, ob)
    sql1 = 'insert into account values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    sql2 = 'insert into amount values(%s,%s,%s)'
    c = con.cursor()
    c.execute(sql1, data1)
    c.execute(sql2, data2)
    con.commit()
    print("DATA ENTERED SUCCESSFULLY")
    main()


def pswd():
    global nam
    nam = input("Enter username:")
    if nam == us:
        wd = input("enter password:")
        if wd == pas:
            print("access granted")
        else:
            print("access denied")
            main()


def depositAmount():
    amount = int(input("Enter deposit amount:"))

    acno = input("Enter account no: ")

    a = "select balance from amount where acno=%s"
    data = (acno,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    tAm = myresult[0] + amount
    sql = "update amount set balance=%s where acno=%s"
    d = (tAm, acno)
    c.execute(sql, d)
    con.commit()
    print("Amount deposited successfully!")
    main()


def withdrawamount():
    amount = int(input("Enter withdraw amount:"))

    acno = input("Enter account no.:")

    a = "select balance from amount where acno=%s"
    data = (acno,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    tAm = myresult[0] - amount
    sql = "update amount set balance=%s where acno=%s"
    d = (tAm, acno)
    c.execute(sql, d)
    con.commit()
    print("Amount withdrawn successfully!")
    main()


def balance():
    acno = input("Enter account no.:")

    a = "select balance from amount where acno = %s"
    data = (acno,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    print("Balance of account: ", acno, "is", myresult[0])
    main()


def displayaccount():
    acno = input("Enter account no.: ")

    a = "select * from account where acno = %s"
    data = (acno,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    for i in myresult:
        print(i, end=" ")
    main()


def closeaccount():
    acno = input("Enter account no.: ")

    sql1 = "delete from account where acno = %s"
    sql2 = "delete from account where acno = %s"
    data = (acno,)
    c = con.cursor()
    c.execute(sql1, data)
    c.execute(sql2, data)
    con.commit()
    main()
    print("Amount closed successfully!")


def main():
    print("""
    1.OPEN NEW ACCOUNT
    2.DEPOSIT AMOUNT
    3.WITHDRAW AMOUNT
    4.BALANCE ENQUIRY
    5.DISPLAY CUSTOMER DETAILS
    6.CLOSE AN ACCOUNT
    """)
    choice = input("Enter task number: ")
    if (choice == '1'):
        openingAccount()

    elif (choice == '2'):
        pswd()
        depositAmount()

    elif (choice == '3'):
        pswd()
        withdrawamount()

    elif (choice == '4'):
        pswd()
        balance()

    elif (choice == '5'):
        mainps()
        pswd()
        displayaccount()

    elif (choice == '6'):
        closeaccount()

    else:
        print("Sorry!! Wrong Choice")
        main()


print("\n**BANK MANAGEMENT PROGRAM**")

psd()
while tr == 0:
    main()
