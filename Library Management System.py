import mysql.connector
import getpass
import time
import sys

login_count = 0

for i in range(1, 4):
    try:
        print("\n")
        passwd = getpass.getpass("Enter the MySQL Client Password: ")
        conobj = mysql.connector.connect(host = 'localhost', user = 'root', password = passwd)

        if conobj.is_connected:
            print("Connected Successfully")
            break

    except mysql.connector.errors.ProgrammingError:
        login_count = login_count + 1
        time.sleep(10)
        print("\nConnection failed, incorrect password entered\n")
        if login_count > 3:
            print("Exiting program due to Security Reasons")
            sys.exit(1)
            break

try:
    cur = conobj.cursor()

except NameError:
    quit()
    

def db_checker():
    '''
    This function checks for the required database.
    If present, uses it
    Else, creates the DataBase with permission from the DataBase Administrator
    '''

    try: 
        cur.execute("show databases")
        db_present = cur.fetchall()
        db_required = ('lib_management',)

        if db_required in db_present:
            pass

        else:
            print("The required database is absent.\n")
            per_1 = input("Do you want to create the database?(Y/n): ")

            if per_1.lower() == 'y':
                print("Creating the DataBase")
                cur.execute('create database lib_management')
                cur.execute('commit')
                print("DataBase created Successfully")

            else:
                print("Program cannot proceed without required database\nExiting Program")
                quit()

        cur.execute('use lib_management')

    except NameError:
        print('Unknown error occurred. Exiting Program')
        quit()

admin_name = input("Enter the name of the Administrator: ")
print('Hello, ', admin_name.capitalize())


def table_checker():
    '''
    This function checks for the required tables
    If present, uses it
    Otherwise
    The table is created when given permission is given by the Database Administrator
    '''

    try:
        cur.execute('show tables')
        present_tables = cur.fetchall()
        required_tables = ('Library', 'Member')

        if required_tables in present_tables:
            print("Required Tables are present in the DataBase\n")
            pass

        elif (('Library',) == present_tables):
            cur.execute('create table Member(Member_Code int, Member_Name varchar(255), Member_Adress varchar(255), Phone int, Max_Limit int, N_O_B_Issued int)')        
            cur.execute('commit')

        elif (('Member',) == present_tables):
            cur.execute('create table Library(Book_Code int, Sub_Code char(200), Title varchar(255), Author varchar(255), Publisher varchar(255), Price int, Member_Code int, Issue_Date datetime)') 
            cur.execute('commit')

        else:
            print('The required tables are not present in the DataBase')
            per_2 = input('Do you wish to create the required tables?(Y/n): ')

            if per_2.lower() == 'y':
                print("Creating the Tables")
                cur.execute('create table Library(Book_Code int PRIMARY KEY, Sub_Code char(200), Title varchar(255), Author varchar(255), Publisher varchar(255), Price int, Member_Code int, Issue_Date datetime)')
                cur.execute('create table Member(Member_Code int PRIMARY KEY, Member_Name varchar(255), Member_Address varchar(255), Phone int, Max_Limit int, N_O_B_Issued int)')
                cur.execute('commit')

            else:
                print("The program cannot proceed without the required tables\nExiting Program")
                quit()

    except NameError:
        print('Unknown Error occurred during execution. Exiting program')
        quit()


print('Starting Initial Check\n\n')


def initial_check():
    '''
    This function runs the initial check.
    Checks for the presence/existence of the required DataBase and Tables
    '''

    time.sleep(2)
    db_checker()
    print('\n\n')
    time.sleep(3)
    table_checker()


print("""\t\tLibrary Table\n
+-----------+----------+-------+--------+-----------+-------+-------------+------------+
| Book_Code | Sub_Code | Title | Author | Publisher | Price | Member_Code | Issue_Date |
+-----------+----------+-------+--------+-----------+-------+-------------+------------+
|           |          |       |        |           |       |             |            |
|           |          |       |        |           |       |             |            |
|           |          |       |        |           |       |             |            |
|           |          |       |        |           |       |             |            |
|           |          |       |        |           |       |             |            |
+-----------+----------+-------+--------+-----------+-------+-------------+------------+
\n\n
""")

print("""\t\tMember Table\n
+-------------+-------------+----------------+-------+-----------+--------------+
| Member_Code | Member_Name | Member_Address | Phone | Max_Limit | N_O_B_Issued |
+-------------+-------------+----------------+-------+-----------+--------------+
|             |             |                |       |           |              |
|             |             |                |       |           |              |
|             |             |                |       |           |              |
|             |             |                |       |           |              |
|             |             |                |       |           |              |
+-------------+-------------+----------------+-------+-----------+--------------+
\n\n""")

def addition_of_records_Member():
    '''
    This function adds additional records to the table titled
    "MEMBER"
    '''
    
    cur.execute('select * from Member')
    prev_row_count = cur.fetchall()
    count_mem_rec_prev = 0
    for i in prev_row_count:
        count_mem_rec_prev += 1

    Mem_Name = input('Enter the name of the Member: ')
    Mem_Code = id(Mem_Name)
    Mem_Address = input("Enter the Address of the Member: ")
    Phone_no = int(input("Enter the Phone number of the member: "))
    Max_limit = int(input("Enter the maximum number of books that can be issued by the member"))
    Issued_books = int(input('Enter the number of books issued by the member: '))

    cur.execute('insert into Member(Member_Code, Member_Name, Member_Address, Phone, Max_Limit, N_O_B_Issued) values({},"{}","{}",{},{},{})'.format(Mem_Code, Mem_Name, Mem_Address, Phone_no, Max_limit, Issued_books))
    cur.execute('commit')

    cur.execute('select * from Member')
    new_row_count = cur.fetchall()
    count_mem_rec_new = 0
    for i in new_row_count:
        count_mem_rec_new += 1

    if (count_mem_rec_new) == (count_mem_rec_prev + 1):
        print("Record added Successfully")
        print('Member Code is: {}'.format(Mem_Code))

    else:
        print("Record not Added")


def addition_of_records_Library():
    '''
    This function adds additional records to the table
    "Library"
    '''

    cur.execute('select * from Library')
    prev_rec_count = cur.fetchall()
    count_lib_rec_prev = 0
    for i in prev_rec_count:
        count_lib_rec_prev += 1
    
    book_title = input("Enter the Title of the Book: ")
    book_code = id(book_title)
    sub_code = input("Enter the Subject Code of the book: ")
    author = input("Enter the name of the Author: ")
    publisher = input("Enter the name of the Publisher: ")
    book_price = int(input("Enter the price of the Book: "))
    m_code = 0
    
    cur.execute('insert into Library(Book_Code, Sub_Code, Title, Author, Publisher, Price, Member_Code) values({}, "{}", "{}", "{}", "{}", {}, {})'.format(book_code, sub_code, book_title, author, publisher, book_price, m_code))
    cur.execute('commit')

    cur.execute('select * from Library')
    new_rec_count = cur.fetchall()
    count_lib_rec_new = 0
    for i in new_rec_count:
        count_lib_rec_new += 1
    
    if (count_lib_rec_new) == (count_lib_rec_prev + 1):
        print('Record Added Successfully')
        print('Book Code is: {}'.format(book_code))
    
    else:
        print("Record not Added")


def modify_records_in_member_table():
    '''
    This function allow the user to modify the "Address" and "Phone Number" of a member in the 
    "MEMBER" table
    '''

    cur.execute('select Member_Code from Member')
    compl_rec = cur.fetchall()
    m_id = int(input("Enter the Member Code: "))
    ty_m_id = (m_id,)
    for i in compl_rec:
        if ty_m_id == i:
            print("User found\n")
            print('\t\tUpdate Menu \n1. Update Address \n2. Update Phone Number \n3. Update Both\n')
            upd_option = int(input("Enter the Update option: "))

            if upd_option == 1:
                new_address = input("Enter the new Address of the Member: ")
                cur.execute('update Member set Member_Address = ("{}") where Member_Code = ({})'.format(new_address, m_id))
                cur.execute('commit')

            elif upd_option == 2:
                new_phone_number = int(input("Enter the new Phone Number of the Member: "))
                cur.execute('update Member set Phone = {} where Member_Code = {}'.format(new_phone_number, m_id))
                cur.execute('commit')

            elif upd_option == 3:
                new_phone_number = int(input("Enter the new Phone Number of the Member: "))
                cur.execute('update Member set Phone = {} where Member_Code = {}'.format(new_phone_number, m_id))
                
                new_address = input("Enter the new Address of the Member: ")
                cur.execute('update Member set Member_Address = "{}" where Member_Code = {}'.format(new_address, m_id))
                
                cur.execute('commit')

            else:
                print("Option entered does not exist in the menu")
        
        else:
            pass


def return_of_books_and_fine_calculator():#Not complete, add the returning book function
    '''
    This function allows the returning of books and calculates the amount to be paid as fine

    If number of days=0 , fine=0
    If number of days<=7 , fine=number of days*0.50
    If number of days<=15 , fine=number of days*1.00
    If number of days>15 , fine=number of days*2.00
    If number of days>0 then
        Display “Member has to pay fine “,fine
        Update member table and library table
    Else
        Display “Bookno not found”
    '''

    max_number_of_days_to_return_the_book = 7

    m_code = int(input("Enter the Member Code: "))
    book_code = int(input("Enter the Book Code: "))

    cur.execute('select Member_Code from Member')
    existing_member_codes = cur.fetchall()

    for i in existing_member_codes:
        if (m_code,) == i:
            print("Member Exists\n")

            cur.execute('select Book_Code from Library where Member_Code = {}'.format(m_code))
            issued_books_by_member = cur.fetchall()

            for j in issued_books_by_member:
                if (book_code,) == j:
                    print("Book Found\n")

                    cur.execute('select curdate()')
                    curdate = cur.fetchall()
                    
                    cur.execute('select Issue_Date from Library where Book_Code = {} and Member_Code = {}'.format(book_code, m_code))
                    issued_date = cur.fetchall()
                    
                    cur.execute('select DATEDIFF({},{})'.format(issued_date, curdate))
                    days_lapsed = cur.fetchall()
                    
                    days = days_lapsed - max_number_of_days_to_return_the_book

                    if days <= 0:
                        print('You have to pay Dhs. 0 as fine\n')
                    
                    elif (days >= 7):
                        print("You have to pay Dhs. ", days * 0.5, 'as fine\n')
                    
                    elif (days >= 15):
                        print('You have to pay Dhs. ', days * 1, 'as fine\n')
                    
                    else:
                        print('You have to pay Dhs. ', days * 2, 'as fine\n')

                else:
                    print("Book Not Found\n")

        else:
            pass

def availability_of_a_certain_book():
    '''
    This function checks for a book
    and 
    Checks its current status -- Available 'A' or Issued 'I'
    '''

    mem_code = int(input("Enter the Member Code"))

    cur.execute('select * from member where Member_Code = {}'.format(mem_code))
    mem_exist = cur.fetchall()

    if (mem_exist,) == ():
        print('Member does not exist')
    
    else:
        book_sub = input("Enter the Subject of the Book: ")
    
        cur.execute('select * from Library where Sub_Code like "{}"'.format(book_sub))
        book_matching_book_sub = cur.fetchall()

        print('Books matching the Subject Code:\n')
        for i in book_matching_book_sub:
            print('Book Code:', i[0])
            print('Subject Code:', i[1])
            print('Title: ', i[2])
            print('Author: ', i[3])
            print('Publisher: ', i[4])
            print("Price: ", i[5])
            print('\n\n')
    

        book_code = int(input("Enter the Book Code: "))

        cur.execute('select * from Library where Sub_Code like ("{}") and Book_Code = {}'.format(book_sub, book_code))

        search_result = cur.fetchall()

        print('Book Search Result')
        for i in search_result:
            print('Book Code:', i[0])
            print('Subject Code:', i[1])
            print('Title: ', i[2])
            print('Author: ', i[3])
            print('Publisher: ', i[4])
            print("Price: ", i[5])
            print('\n\n')


        confirmation_user = input("Is this the book which you want?(Y/n): ")
        book_title = search_result[2]

        cur.execute('select * from member where Member_Code = {}'.format(mem_code))
        mem_details = cur.fetchall()
        max_limit = mem_details[4]
        issued = mem_details[5]

        books_count = max_limit - issued

        if confirmation_user.lower() == 'y':
            cur.execute('select Member_Code from Library where Sub_Code like ("{}") and Book_Code = {}'.format(book_sub, book_code))
            status = cur.fetchall()

            if (status,) == (0,):
                print('The Book is Available\n')

                issue_query = input('Do you want to issue the book?(Y/n): ')

                if issue_query.lower() == 'y':
                    if books_count > 0:
                        print('Issuing Book "{}"'.format(book_title))
                        cur.execute('update Library set Member_Code = {} where Sub_Code like "{}" and Book_Code = {}'.format(mem_code, book_sub, book_code))
                        cur.execute('commit')
                
                    else:
                        print('You cannot issue this book.\nKindly return other book(s) which were issued by you')
                        disp_issued_books = input('Do you want to see the books which are issued under your name?(Y/n): ')

                        if disp_issued_books.lower() == 'y':
                            cur.execute('select Title from Library where Member_Code = {}'.format(mem_code))
                            issued_book_info = cur.fetchall()

                            for i in issued_book_info:
                                print(i)
                                print()

                        else:
                            print('Thanks for using the Issue Service')
        
        else:
            print('The Book is Issued by another member\n')

def book_report():
    '''
    Generates a Book Report which is ordered by
    the Subject of the book
    '''

    print('Book Report')
    cur.execute('select Book_Code int, Sub_Code, Title from Library order by Sub_Code')
    book_result = cur.fetchall()
    count_book_result = 1

    list_subject = []

    for i in book_result:
        print('Results for the Book: ',count_book_result)
        count_book_result += 1

        print('\nBook Code: ', i[0])
        print('Subject Code: ', i[1])
        print('Title: ', i[2])
        print('\n\n')
    
    cur.execute('select DISTINCT(Sub_Code) from Library')
    dist_sub_codes = cur.fetchall()

    for i in dist_sub_codes:
        list_subject.append(i)
    
    print('The Subject Codes which are present currently are: ')
    for i in list_subject:
        print(i)

def books_issued_by_member():
    '''
    This function generates a report which displays 
    the books issued by a member and the member who issued it
    '''

    print('\tBooks Issued by Member Report\n')
    
    book_count = 0

    mem_code_lst = []
    
    cur.execute('select Member_Code from member')
    mem_codes = cur.fetchall()

    for i in mem_codes:
        mem_code_lst.append(i)
    
    for i in mem_code_lst:
        cur.execute('select title from library where Member_Code = {}'.format(i))
        book_rep = cur.fetchall()

        if book_rep == ():
            print('No Books were issued by Member {}'.format(i))
        
        else:
            print('Book(s) issued by Member {} is/are: \n'.format(i))
            for j in book_rep:
                print('Book Title: ',j)
                book_count += 1
            
            print('Number of books issued by Member {} is/are: {}'.format(i, book_count))

def available_books():
    '''
    This function generates a report for
    
    Books which are not issued
    or
    Books which are currently available
    '''

    count_available = 0

    cur.execute('select * from library where Member_Code = 0')
    books_available = cur.fetchall()

    if books_available == ():
        print('None of the books are available.\nAll the books are issued\n')

    else:
        print('The available books is / are: \n')
        
        for i in books_available:
            count_available += 1
            print('Book Code: ', i[0])
            print('Subject Code: ', i[1])
            print('Title: ', i[2])
            print('Author Name: ',i[3])
            print('Publisher: ', i[4])
            print('Price: ', i[5])
            print('\n')
    
        print('There is / are {} available book(s)'.format(count_available))

def book_defaulter():
    '''
    This function displays the defaulters 
    who have not returned their book
    after the 7 day / 1 week issue period
    '''

    max_number_of_days_for_issuing_books = 7
    defaulter_lst = []
    count_defaulters = 0

    cur.execute('select * from library where NOT Member_Code = 0')
    issued_books_result = cur.fetchall()

    cur.execute('select CURDATE()')
    current_date = cur.fetchall()

    for i in issued_books_result:
        cur.execute('select DATEDIFF({}, {}) from library'.format(current_date, i[7]))
        date_difference = cur.fetchall()

        days = date_difference - max_number_of_days_for_issuing_books

        if days <= 0:
            pass

        else:
            count_defaulters += 1
            defaulter_lst.append(i[6])
    
    print('There is / are {} defaulter(s)'.format(count_defaulters))

    if count_defaulters == 0:
        pass

    else:
        print('The list of defaulter(s) is / are as follows: \n')
        for i in defaulter_lst:
            print(i)

def members_in_the_library():
    '''
    This function displays all the 
    Members in the library
    along with their "Member Code"
    '''

    count_member = 0
    cur.execute('select Member_Code, Member_Name from member')
    member_result = cur.fetchall()

    for i in member_result:
        print('Member Code: {}\nMember Name: {}\n'.format(i[0], i[1]))
        count_member += 1
    
    print('There are {} registered members'.format(count_member))

def Report_of_DataBase():
    '''
    This function generates a report which consists of the following
    1) Subject wise book list
    2) List of books issued to members
    3) List of available books
    4) List of defaulters
    5) List of members in the library
    '''

    print('\t\tReport Menu')
    print('\n1. Book Report ordered by the Subject\n2. List of Books issued to Members\n3. List of Available Books\n4. List of Defaulters')
    print('\n5. List of Members')
    print()

    report_option = int(input('Enter your choice: '))

    if report_option == 1:
        book_report()

    elif report_option == 2:
        books_issued_by_member()

    elif report_option == 3:
        available_books()

    elif report_option == 4:
        book_defaulter()

    elif report_option == 5:
        members_in_the_library()

    else:
        print('Invalid Option Entered')

ans = 'y'
while ans.lower() == 'y':
    print('\t\t\t\tMain Menu\n\n')
    print('1. Addition of Books\n2. Addition of Members\n3. Modifying Records\n4. Modifying Member info\n5. Issue Book\n6. Return Books')
    print('7. Availability of a certain book\n8. Report\n\n')

    choice = int(input("Enter your choice: "))

    


print('Closing connection to Server DataBase in....')
for i in range(3, 0, -1):
    print(i, '\n')
    time.sleep(1)

print('Connection Closed Successfully')

cur.close()