import mysql.connector
import time
import getpass

login_count = 0

for i in range(0, 2):
    try:
        print("\n")
        passwd = getpass.getpass("Enter the MySQL Client Password: ")
        conobj = mysql.connector.connect(host = 'localhost', user = 'root', password = passwd)

        if conobj.is_connected:
            print("Connected Successfully")
            break

        else:
            print("Password Entered is Incorrect\n")
            login_count = login_count + 1
        
            if login_count == 3:
                print("\nPassword Entered Incorrectly 3 times")
                time.sleep(5)
                print('\nExiting Program')            
                exit()

        print(login_count)

    except mysql.connector.errors.ProgrammingError:
        print("\nConnection failed, incorrect password entered\n")
        if login_count == 3:
            exit()

try:
    cur = conobj.cursor()

except NameError:
    print("This program requires Authorisation / DataBase Admin Password")

admin_name = input("Enter the administrator name: ")
print("Welcome", admin_name.capitalize())

print("Table Sample:")
print("""
_______________________________________________________
|Sr. No| Customer ID | Account Number | Customer Name |
|------+-------------+----------------+---------------|
|      |             |                |               |
|      |             |                |               |
|      |             |                |               |
|      |             |                |               |
|      |             |                |               |
|------+-------------+----------------+---------------|
\n""")

def db_creation():
    '''
    This function creates the MySQL Bank Management DataBase
    '''

    cur.execute('show databases')
    pre_existing_db = cur.fetchall()
    req_db = 'banking_db'

    if (req_db, ) in pre_existing_db:
        print("The required DataBase exists in the Client")
    
    else:
        print("Creating the Bank DataBase")
        cur.execute("create database banking_db")
        cur.execute('commit')
    
    cur.execute('use banking_db')

db_creation()

def table_creation():
    '''
    This function creates a table within the Banking DataBase
    '''

    cur.execute('show tables')
    pre_existing_tables = cur.fetchall()
    req_tables = ('customer_details', )

    if req_tables in pre_existing_tables:
        print("Requirement already Satisfied")
    
    else:
        print("Creating the Customer Table")
        cur.execute("create table customer_details(Customer_ID int, Customer_Name varchar(255), Account_Number int, Account_Balance int)")
        cur.execute('commit')

table_creation()

def account_balance_checker():
    '''
    This function checks for the balance in the Customer's account
    '''

    customer_account_no = int(input("Enter the Account Number of the Customer: "))
    cur.execute('select * from customer_details where Account_Number = %i;' %(customer_account_no))

    record = cur.fetchall()

    for i in record:
        print("Customer Name: ", i[1])
        print("BALANCE: ", i[3])


def account_creation():
    '''
    This function creates a new Bank account for a Customer
    '''
    cus_name = input("Enter the First Name of the customer: ")
    name = cus_name.capitalize()

    cus_id = int(input('Enter the customer ID: '))

    acc_no = int(input("Enter an account number: "))

    acc_bal = int(input('Enter the current account balance: '))


    cur.execute('insert into customer_details(Customer_ID, Customer_Name, Account_Number, Account_Balance) values ({}, "{}", {}, {});'.format(cus_id, name, acc_no, acc_bal))
    cur.execute('commit')


def del_account():
    '''
    This function deletes an existing Bank Account from the database
    '''

    account_no = int(input("Enter the Account Number: "))
    confirmation = input("Are you sure?(Y/n): ")
    
    if confirmation.lower() == 'y':
        del_account_cmd = 'delete from customer_details where Account_Number = %s' %(account_no)
        cur.execute(del_account_cmd)
        cur.execute('commit')
    
    else:
        print("Request Cancelled")


def display_details():
    '''
    This function prints/displays the details of a bank account
    '''

    account_no = int(input("Enter Account Number: "))

    retrieve_record = 'select * from customer_details where Account_Number = %s' %(account_no)
    cur.execute(retrieve_record)
    details = cur.fetchall()

    for i in details:
        print("CUSTOMER DETAILS FOR ACCOUNT NUMBER:", account_no," \n")
        print("CUSTOMER ID:", i[0])
        print("NAME:", i[1])
        print("ACCOUNT NUMBER:", i[2])
        print("ACCOUNT BALANCE:", i[3])

ans = 'y'
while ans.lower() == 'y':
    print("\n\t\t\t\t\tMAIN MENU\n")
    print('1. Check for Balance in an account \n2. Create a new account \n3. Delete an account \n4. Display Account Details\n')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_balance_checker()
    
    elif choice == 2:
        account_creation()

    elif choice == 3:
        del_account()

    elif choice == 4:
        display_details()

    else:
        print("Invalid Menu option entered")
    
    print()
    ans = input("Do you wish to continue?(Y/n): ")
    print()

conobj.close()