def C_to_F(x):
    '''
    This function converts the temperature entered from

    Degree Celsius(C) to Degree Fahrenheit(F)
    '''

    C = (5 * (x - 32))/9
    
    return C


def F_to_C(x):
    '''
    This function converts the temperature entered from

    Degree Fahrenheit(F) to Degree Celsius(C)
    '''

    F = ((9 * x) / 5) + 32

    return F


ans = 'y'

while ans.lower() == 'y':

    print("\t\t\tMain Menu\n")
    print("1. Degree C to Degree F \n2. Degree F to Degree C\n")

    choice = int(input("Enter your choice: "))

    print()
    temp = float(input("Enter temperature: "))
    print()

    if choice == 1:
        print("The temperature ", temp, 'C to F is: ', C_to_F(temp), 'F')

    elif choice == 2:
        print("The temperature ", temp, 'F to C is: ', F_to_C(temp), 'C')

    else:
        print("Option entered is INVALID\n")

    ans = input("Do you wish to continue(Y/n): ")
