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

cur = conobj.cursor()

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

    pre_existing_db = cur.fetchall('show databases')
    req_db = 'banking_db'

    if (req_db, ) in pre_existing_db:
        print("The required DataBase exists in the Client")
    
    else:
        print("Creating the Bank DataBase")
        cur.execute("create database banking_db")
        cur.execute('commit')
    
    cur.execute('use banking_db')

def table_creation():
    '''
    This function creates a table within the Banking DataBase
    '''

    pre_existing_tables = cur.fetchall('show tables')
    req_tables = ('customer_details', )

    if req_tables in pre_existing_tables:
        print("Requirement already Satisfied")
    
    else:
        print("Creating the Customer Table")
        cur.execute("create table customer_details(Customer_ID int, Customer_Name varchar(255), Account_Number int, Customer_Age int)")

def account_balance_checker():
    '''
    This function checks for the balance in the Customer's account
    '''


ans = 'y'
while ans.lower() == 'y':
    print("\n\t\t\t\t\tMAIN MENU\n")
    print('1. Check for Balance in an account \n2. Create a new account \n3. Delete an account \n4. Display Account Details\n')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pass
    
    elif choice == 2:
        pass

    elif choice == 3:
        pass

    elif choice == 4:
        pass

    else:
        print("Invalid Menu option entered")
    
    print()
    ans = input("Do you wish to continue?(Y/n): ")
    print()