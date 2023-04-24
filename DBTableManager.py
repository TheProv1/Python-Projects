import mysql.connector
import time
import sys

conobj_var = ''

def login(db_pass):
    '''
    This function runs the login process, giving the user 3 chances to enter the password.
    If the password is entered incorrectly 3 times, the programs exits.
    '''
    
    global conobj_var
    
    time_delay = 5
    login_count = 1
    for i in range(0,3):
        try:
            conobj = mysql.connector.connect(host = 'localhost', user = 'root', password = db_pass)
            conobj_var = conobj

            if conobj.is_connected:
                print('Connected Successfully')
                conobj_var = conobj
                break
            
        except mysql.connector.errors.ProgrammingError:
            login_count += 1
            time.sleep(time_delay)

            if login_count >= 3:
                print('Exiting Program, password entered incorrectly')
                sys.exit(1)
                break


def db_creator(db_name):
    '''
    This function creates the DataBase.
    If absent, it creates the DataBase,
    else, it uses the existing database.
    '''
    
    cur = conobj_var.cursor()
    cur.execute('show databases')
    db_present = cur.fetchall()

    if (db_name,) in db_present:
        print('Database: {} is present in the client'.format(db_name))
        print('\nSwitching to DataBase: {}'.format(db_name))
        cur.execute('use {}'.format(db_name))

    else:
        print('The database does not exist in the system. Do you want to create it?(Y/n): ')
        db_create = input()
        
        if db_create.lower() == 'y':
            cur.execute('create database {}'.format(db_name))
            cur.execute('commit')
            cur.execute('use {}'.format(db_name))
        
        else:
            print('Exiting Program')
            cur.close()
            sys.exit(1)


def db_remover(db_name):
    '''
    This function removes the DataBase.
    If absent, it displays an error message,
    else, it deletes the DataBase.
    '''

    cur = conobj_var.cursor()
    cur.execute('show databases')
    db_present = cur.fetchall()

    if (db_name,) in db_present:
        print('DataBase: {} is present in the Client'.format(db_name))
        print('\nRemoving DataBase, this action cannot be undone')










