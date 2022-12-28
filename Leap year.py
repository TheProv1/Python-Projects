ans = 'y'

while ans.lower() == 'y':
    print("\t\t\t\tMENU\n")

    year = int(input("Enter the year: "))

    if (year % 4 == 0) and (year % 100 == 0):
        print("\nThe year entered is a: CENTENNIAL YEAR")

    elif (year % 4 == 0):
        print("\nThe year entered is a: LEAP YEAR")

    else:
        print("\nThe year entered is: NOT A LEAP YEAR")
    
    ans = input("\nDo you wish to continue?(Y/n): ")
    print("\n")