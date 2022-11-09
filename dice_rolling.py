import random

def single_die():
	'''
	This function gives a random value of the die (1-6)
	'''
	
	die_roll = random.randint(1,6)
	return die_roll

def double_dice():
	'''
	This function uses the previous function (single_die()) twice
	'''
	
	val_1 = single_die()
	val_2 = single_die()
	return val_1, val_2

num1, num2 = double_dice()

sum_faces = num1 + num2

print("\t\t\tMENU")
print("\n1. One Die\n2. Two Dice\n")

ans = 'y'
while ans.lower() == 'y':
	option = int(input("Enter your choice: "))
	
	if option == 1:
		print("The value of the face is: ",single_die())
	
	elif option == 2: 
		print("The value of the first face is: ",num1, "\nand the value of the second face is: ",num2)
		print()
		print("The sum of the faces is: ",sum_faces)
	
	ans = input("Do you wish to continue?(Y/n): ")
	print("\n")
	
