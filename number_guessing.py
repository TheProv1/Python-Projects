import random

n = int(input("Enter the end range: "))
num = random.randint(0,n+1)

guessed_numbers = []

print("\nYou have 5 chances in total to guess the number from 0 to ",n)
print()

ans = 'y'
while ans.lower() == 'y':
	chances = 5
	
	while chances > 0:
		user_num = int(input("Enter your guessed number: "))
	
		if num == user_num:
			print("You have guessed the number correctly. Congrats")
			exit()
	
		else:
			guessed_numbers.append(user_num)
			print("The entered number is not correct try again.")
			print("\n")
			chances -= 1
			print("Number of chance(s) left: ", chances)
	
	print("The number(s) entered is/are: ", guessed_numbers)
	
	print("\nThe number to be guessed was: ", num)
	
	ans = input("Do you wish to continue?(Y/n): ")
	print("\n")
