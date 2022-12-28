P = int(input("Enter the Principle Amount: "))
Rate = int(input("Enter the Interest Rate: "))
T = int(input("Enter the Time Period in terms of year(s): "))

R = Rate / 100

interest = P * R * T

print("The Interest to be paid is: ", interest)

print("\nTotal Payable amount: ", interest + P)
