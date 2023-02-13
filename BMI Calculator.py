def user_mass():
    
    user_weight = float(input('Enter your weight: '))
    weight_unit = input('Is the weight entered in Pounds or Kg?(Enter (P) or (Kg)): ')

    if weight_unit.lower() == 'p':
        weight = user_weight * 0.4535

    elif weight_unit.lower() == 'kg':
        weight = user_weight

    return weight

def user_height():
    
    height_choice = input('Do you want to enter your height in (Feet, Inches (F)) or (cm (c)): ')

    if height_choice.lower() == 'f':
        feet = int(input('Enter the "feet" component: '))
        inch = int(input('Enter the "inch" component: '))

        height = (feet * 30.48) + (inch * 2.54)
    
    elif height_choice.lower() == 'c':
        height = float(input('Enter height: '))

    height_in_m = height/100

    return height_in_m

try:
    bmi = (user_mass()/((user_height())**2))

    if bmi <= 16:
        print('Severly Underweight')
    
    elif bmi <= 18.5:
        print('Underweight')
    
    elif bmi <= 25:
        print('Healthy')
    
    elif bmi <= 30:
        print("Overweight")

except ZeroDivisionError:
    print('Division By Zero is not Possible.\nEnter the correct height')