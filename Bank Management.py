import mysql.connector
import time

login_count = 0

for i in range(0, 2):
    
    print("\n")
    passwd = input("Enter the MySQL Client Password: ")
    conobj = mysql.connector.connect(host = 'localhost', user = 'root', password = passwd)

    if conobj.is_connected:
        print("Connected Successfully")
        break

    else:
        print("Password Entered is Incorrect\n")
        login_count += 1
        
        if login_count == 3:
            print("\nPassword Entered Incorrectly 3 times")
            time.sleep(1)
            print('\nExiting Program')            
            exit()

