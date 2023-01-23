import mysql.connector
import time
import getpass
import sys

login_count = 0

for i in range(0, 3):
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
        
            if login_count > 3:
                print("\nPassword Entered Incorrectly 3 times")
                time.sleep(5)
                print('\nExiting Program')            
                sys.exit(1)
                break

        print(login_count)

    except mysql.connector.errors.ProgrammingError:
        print("\nConnection failed, incorrect password entered\n")
        if login_count > 3:
            sys.exit(1)
            break

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
    try:
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

    except NameError:
        quit()

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

    acc_no = id(name)

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

min_balance = 2500

def transfer_function():
    '''
    This function transfers an amount 'x' from account "A" to account "B"
    '''
    remitter_account_no = int(input("Enter the Remitter Account Number: "))
    beneficiary_account_no = int(input("Enter the Beneficiary Account Number: "))
    amount_x = int(input("Enter the amount to be transfered: "))

    cur.execute('select Account_Balance from customer_details where Account_Number = %d' %(remitter_account_no))
    remitter = cur.fetchall()
    bal = remitter[0][0]
    if (bal - amount_x) > min_balance:
        cmd_upd_rem = 'update customer_details set Account_Balance = Account_Balance - %s' %(amount_x) + ' where Account_Number = %s' %(remitter_account_no)
        cmd_upd_ben = 'update customer_details set Account_Balance = Account_Balance + %s' %(amount_x) + ' where Account_Number = %s' %(beneficiary_account_no)
        cur.execute(cmd_upd_rem)
        cur.execute(cmd_upd_ben)
        cur.execute('commit')
        time.sleep(5)
        print("\nTransaction Completed Successfully")

    else:
        print("Transaction cannot continue. Account Balance is less than minimum balance.")

def deposit_function():
    '''
    This function deposits an amount 'x' into an Account
    '''
    dep_amt = int(input("Enter the amount to be deposited: "))
    account = int(input("Enter the Account to deposit the amount: "))
    cmd_upd_bal = 'update customer_details set Account_Balance = Account_Balance + %s' %(dep_amt) + ' where Account_Number = %s' %(account)
    cur.execute(cmd_upd_bal)
    cur.execute('commit')

    time.sleep(5)

    print("Money Deposited Successfully")
    
    
def withdraw_function():
    '''
    This function withdraws an amount 'x' from an Account
    '''

    try:
        withdraw_amt = int(input("Enter the amount to be withdrawn: "))
        account = int(input("Enter the Account Number to withdraw the amount: "))
        cmd_upd_bal = 'update customer_details set Account_Balance = Account_Balance - %d' %(withdraw_amt) + ' where Account_number = %s' %(account)
        cur.execute(cmd_upd_bal)
        cur.execute('commit')

        print("Money Withdrawn Successfully")

    except AttributeError:
        print("Un Unknown Error has caused the program from executing properly")

ans = 'y'
while ans.lower() == 'y':
    print("\n\t\t\t\t\t\tMAIN MENU\n")
    print('1. Account Management \n2. Transactions\n')

    main_menu_choice = int(input("Enter your choice: "))
    print()

    if main_menu_choice == 1:
        
        print('\t\t\tAccount Management\n\n1. Check for Balance in an account \n2. Create a new account \n3. Delete an account \n4. Display Account Details\n')
        acc_choice = int(input("Enter your choice: "))

        if acc_choice == 1:
            account_balance_checker()
    
        elif acc_choice == 2:
            account_creation()

        elif acc_choice == 3:
            del_account()

        elif acc_choice == 4:
            display_details()

        else:
            print("Invalid Option Entered")
    
    elif main_menu_choice == 2:
        
        print('\t\t\tTransactions\n1. Transfer Money \n2. Depositing Money \n3. Withdrawing Money')
        tra_choice = int(input("Enter your choice: "))

        if tra_choice == 1:
            transfer_function()

        elif tra_choice == 2:
            deposit_function()

        elif tra_choice == 3:
            withdraw_function()

        else:
            print("Invalid Option Entered")

    else:
        print("Invalid Main-Menu Option Entered")

    print()
    ans = input("Do you wish to continue?(Y/n): ")
    print()

conobj.close()