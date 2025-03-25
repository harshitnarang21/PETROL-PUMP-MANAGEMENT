import mysql.connector
from tabulate import tabulate
from datetime import date

#Function to add customer details
def addcustomer():
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    q='select * from customer'
    curobj.execute(q)
    data=curobj.fetchall()
    if data==[]:
        cn=1
    else:
        cn=data[-1][0]+1
    print('CUSTOMER ID:',cn)
    cname=input('Enter the name of the customer:')
    while True:
        phone=input('Enter the phone number of the customer:')
        if len(phone)!=10 or phone.isdigit()==False:
            print("Invalid Phone Number!")
            print("Please enter again!")
        else:
            break
    points=0
    q='insert into customer values({},"{}","{}",{})'.format(cn,cname,phone,points)
    curobj.execute(q)
    conobj.commit()
    print("Record added successfully!")
    conobj.close()
   
#Function to search customer details by ID
def searchbyid():
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    cno=input('Enter the Customer ID:')
    curobj.execute("Select * from customer where cno='{}'".format(cno))
    a=curobj.fetchall()
    if a==[]:
        print('Record not present!')
    else:
        print('\t\tCustomer Details')
        print('\t\t----------------')
        print(tabulate(a,headers=['CUSTOMERNO','NAME','PHONE']))
    conobj.close()
    
#Function to search customer details by Phone Number
def searchbyphone():
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',database='PETROLPUMPdb')
    curobj=conobj.cursor()
    while True:
        phone=input('Enter the phone number of the customer:')
        if len(phone)!=10 or phone.isdigit()==False:
            print("Invalid Phone Number!")
            print("Please enter again!")
        else:
            break
    curobj.execute("Select * from customer where phone='{}'".format(phone))
    a=curobj.fetchall()
    if a==[]:
        print('\nRecord not present!')
    else:
        print('\t\tCustomer Details')
        print('\t\t----------------')
        print(tabulate(a,headers=['CUSTOMERNO','NAME','PHONE NUMBER'],\
                       tablefmt='fancy_grid'))

    conobj.close()
    
#Function to display customer details
def displaycustomer():
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    curobj.execute('Select* from customer')
    a=curobj.fetchall()
    print()
    print('\t\tCustomer Details')
    print('\t\t----------------')
    print(tabulate(a,headers=['CUSTOMERNO','NAME','PHONE NUMBER'],\
                   tablefmt='fancy_grid'))
    conobj.close()

#Function to modify customer phone number
def modifyphone():
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    id=int(input("Enter the customer ID :"))
    curobj.execute("Select * from customer where cno={}".format(id))
    data=curobj.fetchall()
    if data==[]:
           print("\nCustmor Id does not exists!")
    else:
        print()
        print('\t\tCustomer Details')
        print('\t\t----------------')
        print(tabulate(data,headers=['CUSTOMERNO','NAME','PHONE NUMBER'],\
                       tablefmt='fancy_grid'))
        while True:
            phone=input('Enter the new phone number of the customer:')
            if len(phone)!=10 or phone.isdigit()==False:
                print("Invalid Phone Number!")
                print("Please enter again!")
            else:
                break
        q='update customer set phone="{}" where cno={}'.format(phone,id)
        curobj.execute(q)
        print("Customer Phone Number updated!")
        conobj.commit()
    conobj.close()

#Function to modify customer phone name
def modifyname():
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    id=int(input("Enter the customer ID :"))
    curobj.execute("Select * from customer where cno={}".format(id))
    data=curobj.fetchall()
    if data==[]:
           print("\nCustmor Id does not exists!")
    else:
        print()
        print('\t\tCustomer Details')
        print('\t\t----------------')
        print(tabulate(data,headers=['CUSTOMERNO','NAME','PHONE NUMBER'],\
                       tablefmt='fancy_grid'))
        name=input('Enter the new name of the customer:')
        q='update customer set cname="{}" where cno={}'.format(name,id)
        curobj.execute(q)
        print("Customer Name updated!")
        conobj.commit()
    conobj.close()
    
#Function to search customer details
def search():
    while True:
        print()
        print("\t\tHP PETROLEUM LTD.")
        print("\t\tCUSTOMER - MENU")
        print()
        print("1.Search customer by ID")
        print("2.Search customer by Phone")
        print("3.Back to Customer menu")
        option=int(input("Enter your choice: "))
        if option==1:
            searchbyid()
        elif option==2:
            searchbyphone()
        elif option==3:
            return
        else:
            print("Wrong menu option!")
            print("Try again")
        opt=input("Do you want to continue with Customer Search?")
        if opt=='n' or opt=='N':
            break

#Function to modify customer details
def modify():
    while True:
        print()
        print("\t\tHP PETROLEUM LTD.")
        print("\t\tCUSTOMER - MENU")
        print()
        print("1.Modify Customer Name")
        print("2.Modify Customer Phone Number")
        print("3.Back to Customer menu")
        option=int(input("Enter your choice: "))
        if option==1:
            modifyname()
        elif option==2:
            modifyphone()
        elif option==3:
            return
        else:
            print("Wrong menu option!")
            print("Try again")
        opt=input("Do you want to continue with Customer detail Modifications?Y/N")
        if opt=='n' or opt=='N':
            break
    
#Function for customer menu
def customer_menu():
    while True:
        print()
        print("\t\tHP PETROLEUM LTD.")
        print("\t\t CUSTOMER - MENU")
        print()
        print("1.New Customer")
        print("2.Search Customer Details")
        print("3.Modify Customer Details")
        print("4.Display all customers")
        print("5.Back to Main-Menu")
        choice=int(input("Enter your choice: "))
        print()
        if choice==1:
            addcustomer()
        elif choice==2:
            search()
            continue
        elif choice==3:
            modify()
            continue
        elif choice==4:
            displaycustomer()
        elif choice==5:
            break
        else:
            print("Wrong menu option!")
            print("Try again")
        option=input("\nDo you want to continue with Customer Menu?")
        if option=='n' or option=='N':
            break         

#Function to add fuel rates
def add_fuel_rate():
    print()
    print("\t\tHP PETROLEUM LTD.")
    print("\t\t  ADMIN - MENU")
    print()
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',database='PETROLPUMPdb')
    curobj=conobj.cursor()
    print('TODAY\'S DATE :',date.today())
    todate=date.today()
    q='select * from fuel where tdate="{}"'.format(todate)
    curobj.execute(q)
    data=curobj.fetchall()
    if data==[]:
        normalpetrol=float(input('Enter Today\'s NORMAL PETROL  PRICE : '))
        powerpetrol=float(input('Enter Today\'s POWER PETROL PRICE : '))
        diesel=float(input('Enter Today\'s DIESEL  PRICE : '))
        q="insert into fuel values('{}',{},{},{})".format(todate,normalpetrol,powerpetrol,diesel)
        curobj.execute(q)
        conobj.commit()
        print("\nToday's Fuel Rates saved!")
    else:
        print()
        print("\nToday's Fuel Rates already available!\n")
        print(tabulate(data,headers=['DATE','NORMAL PERTOL\nRATE','POWER PETRO0o[L\nRATE',\
                                     'DIESEL RATE'],tablefmt='fancy_grid'))
    conobj.close()
    
#Function to update fuel rates        
def update_fuel_rate():
    print()
    print("\t\tHP PETROLEUM LTD.")
    print("\t\t  ADMIN - MENU")
    print()
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    print('TODAY\'S DATE :',date.today())
    todate=date.today()
    q='select * from fuel where tdate="{}"'.format(todate)
    curobj.execute(q)
    data=curobj.fetchall()
    if data==[]:
        print("Today's fuel rate not available!")
    else:
        print()
        print(tabulate(data,headers=['DATE','NORMAL PERTOL\nRATE',\
                                     'POWER PETROL\nRATE','DIESEL RATE'],\
                                       tablefmt='fancy_grid'))
        normalpetrol=data[0][1]
        powerpetrol=data[0][2]
        diesel=data[0][3]
        choice=input("Do you want to modify Normal Petrol Rate? Y/N")
        if choice=='y' or choice=='Y':
            normalpetrol=float(input('Enter Today\'s NORMAL PETROL  PRICE : '))
        choice=input("Do you want to modify Power Petrol Rate? Y/N")
        if choice=='y' or choice=='Y':
            powerpetrol=float(input('Enter Today\'s POWER PETROL PRICE : '))
        choice=input("Do you want to modify Diesel Rate? Y/N")
        if choice=='y' or choice=='Y':
            diesel=float(input('Enter Today\'s DIESEL  PRICE : '))
        q="update fuel set normalpetrol={}, powerpetrol={},diesel={} \
            where tdate='{}'".format(normalpetrol,powerpetrol,diesel,todate)
        curobj.execute(q)
        conobj.commit()
        conobj.close()
        print("\nToday's Fuel Rates modified!")

#Function to display fuel rates
def display_fuel_rate():
    print()
    print("\t\tHP PETROLEUM LTD.")
    print("\t\t  ADMIN - MENU")
    print()
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    print('TODAY\'S DATE :',date.today())
    todate=date.today()
    q='select * from fuel where tdate="{}"'.format(todate)
    curobj.execute(q)
    data=curobj.fetchall()
    if data==[]:
        print("Today's fuel rate not available!")
    else:
        print()
        print(tabulate(data,headers=['DATE','NORMAL PERTOL\nRATE',\
                                     'POWER PETROL\nRATE','DIESEL RATE'],\
                                       tablefmt='fancy_grid'))
    conobj.close()
    
def del_fuel_rate():
    print()
    print("\t\tHP PETROLEUM LTD.")
    print("\t\t  ADMIN - MENU")
    print()
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    print('TODAY\'S DATE :',date.today())
    todate=date.today()
    q='select * from fuel where tdate="{}"'.format(todate)
    curobj.execute(q)
    data=curobj.fetchall()
    if data==[]:
        print("Today's fuel rate not available!")
    else:
        print()
        print(tabulate(data,headers=['DATE','NORMAL PERTOL\nRATE',\
                                     'POWER PETROL\nRATE','DIESEL RATE'],\
                                       tablefmt='fancy_grid'))
        choice=input("\nAre you sure to delete today's fuel rate?Y/N")
        if choice=='y' or choice=='Y':
            q='delete from fuel where tdate="{}"'.format(todate)
            curobj.execute(q)
            conobj.commit()
    conobj.close()
            
#Function to search fuel rates
def search_fuel_rate():
    print()
    print("\t\tHP PETROLEUM LTD.")
    print("\t\t  ADMIN - MENU")
    print()
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    print('TODAY\'S DATE :',date.today())
    todate=input("\nEnter date to view fuel rates :(yyyy-mm-dd)")
    q='select * from fuel where tdate="{}"'.format(todate)
    curobj.execute(q)
    data=curobj.fetchall()
    if data==[]:
        print("Fuel rate not available for ",todate)
    else:
        print()
        print(tabulate(data,headers=['DATE','NORMAL PERTOL\nRATE',\
                                     'POWER PETROL\nRATE','DIESEL RATE'],\
                                       tablefmt='fancy_grid'))
    conobj.close()
    
#Function to display revenue of a particular date
def date_revenue():
    print()
    print("\t\tHP PETROLEUM LTD.")
    print("\t\t ADMIN - MENU")
    print("\t\t REPORTS-MENU")
    print("\t\t ------------")
    print()
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPdb')
    curobj=conobj.cursor()
    print('DATE :',date.today())
    todate=input("\nEnter date(yyyy-mm-dd) :")
    q='select fuel_type,sum(amount) from revenue \
        where date_refill="{}" group by fuel_type'.format(todate)
    curobj.execute(q)
    data=curobj.fetchall()
    print(tabulate(data,headers=['FUEL-TYPE','TOTAL AMOUNT'],\
                                 tablefmt='fancy_grid'))
    q='select sum(amount) from revenue where date_refill="{}"'\
       .format(todate)
    curobj.execute(q)
    data=curobj.fetchall()
    print("\nTOTAL REVENUE FOR DATE ",todate," is Rs. ", data[0][0])
    conobj.close()

#Function to display revenue between given dates
def date_range_revenue():
    print()
    print("\t\tHP PETROLEUM LTD.")
    print("\t\t ADMIN - MENU")
    print("\t\t REPORTS-MENU")
    print("\t\t ------------")
    print()
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPDB')
    curobj=conobj.cursor()
    print('DATE :',date.today())
    sdate=input("\nEnter starting date(yyyy-mm-dd) :")
    edate=input("\nEnter ending date(yyyy-mm-dd) :")
    q='select fuel_type,sum(amount) from revenue \
        where date_refill between "{}" and "{}" group by fuel_type'\
        .format(sdate,edate)
    curobj.execute(q)
    data=curobj.fetchall()
    print(tabulate(data,headers=['FUEL-TYPE','TOTAL AMOUNT'],\
                                 tablefmt='fancy_grid'))
    q='select sum(amount) from revenue where date_refill between "{}" and "{}"'\
        .format(sdate,edate)
    curobj.execute(q)
    data=curobj.fetchall()
    print("\nTOTAL REVENUE BETWEEN ",sdate,"and ", edate," is Rs. ", data[0][0])    
    conobj.close()




#Function for report menu
def reports():
    while True:
        print()
        print("\t\tHP PETROLEUM LTD.")
        print("\t\t ADMIN - MENU")
        print("\t\t REPORTS-MENU")
        print("\t\t ------------")
        print()
        print("1.Total Revenue of a particular date")
        print("2.Back to Admin-Menu")
        choice=int(input("Enter your choice: "))
        print()
        if choice==1:
            date_revenue()
        elif choice==2:
            break
        else:
            print("Wrong menu option!")
            print("Try again")
        option=input("\nDo you want to continue with REPORT MENU? Y/N")
        if option=='n' or option=='N':
            break  
    
#Function for admin menu        
def admin_menu():
    while True:
        print()
        print("\t\tHP PETROLEUM LTD.")
        print("\t\t  ADMIN - MENU")
        print()
        print("1.Add today's rate")
        print("2.Update today's fuel rates ")
        print("3.Delete today's fuel rates")
        print("4.Display today's fuel rates")
        print("5.Back to Main-Menu")
        choice=int(input("Enter your choice: "))
        print()
        if choice==1:
            add_fuel_rate()
        elif choice==2:
            update_fuel_rate()
            continue
        elif choice==3:
            del_fuel_rate()
        elif choice==4:
            display_fuel_rate()
        elif choice==5:
            break
        else:
            print("Wrong menu option!")
            print("Try again")
        option=input("\nDo you want to continue with ADMIN MENU? Y/N")
        if option=='n' or option=='N':
            break             

#Function to refilling fuel in a vehicle
def fuel_refill():
    print()
    print("\t\tHP PETROLEUM LTD.")
    print("\t\t   REFILL FUEL")
    print("\t\t   -----------")
    print()
    conobj=mysql.connector.connect(host='localhost',user='root',passwd='1478',\
                                   database='PETROLPUMPDB')
    curobj=conobj.cursor()
    print('TODAY\'S DATE :',date.today())
    todate=date.today()
    id=int(input("\nEnter the customer ID :"))
    curobj.execute("Select * from customer where cno={}".format(id))
    data=curobj.fetchall()
    if data==[]:
        print("\nCustmor Id does not exists!")
    else:
        q='select * from fuel where tdate="{}"'.format(todate)
        curobj.execute(q)
        data1=curobj.fetchall()
        while True:
            print("\n\tFUEL TYPES")
            print("   \t----------")
            print("[1]NORMAL PETROL")
            print("[2]POWER PETROL")
            print("[3]DIESEL")
            t=int(input("Select the Fuel Type :"))
            if t==1:
                rate=data1[0][1]
                ftype="NORMAL PETROL"
                break
            elif t==2:
                rate=data1[0][2]
                ftype="POWER PETROL"
                break
            elif t==3:
                rate=data1[0][3]
                ftype="DIESEL"
                break
            else:
                print("Wrong fuel type!\nEnter again")
                continue
        amt=float(input("\nEnter the amount for fuel refilling :Rs. "))
        q = amt / float(rate)

        print("\nPetrol Quantity=",f'{q:.2f}'," litres")
        p=amt//100
        print("\n",round(p)," points added to ", data[0][1]," card.")
        q="update customer set points=points+{} where cno={}".format(p,id)
        curobj.execute(q)
        conobj.commit()
        q="insert into revenue values('{}','{}',{})".format(todate,ftype,amt)
        curobj.execute(q)
        conobj.commit()
    conobj.close()
                  
#Function for main menu
def main_menu():
    while True:
        print()
        print("\t\tHP PETROLEUM LTD.")
        print("\t\t  MAIN - MENU")
        print()
        print("1.ADMIN")
        print("2.CUSTOMER")
        print("3.FUEL REFILLING")
        print("4.QUIT")
        choice=int(input("Enter your choice: "))
        print()
        if choice==1:
            admin_menu()
            continue
        elif choice==2:
            customer_menu()
            continue
        elif choice==3:
            fuel_refill()
        elif choice==4:
            break
        else:
            print("Wrong menu option!")
            print("Try again")
        option=input("\nDo you want to continue with MAIN MENU?Y/N")
        if option=='n' or option=='N':
            break
        
        
main_menu()
