# Let’ write a program to divide up the check among diners in a party.

# Write a program to input the amount of a restaurant check, tip %, and number of diners
check_amount = float(input("Enter the amount of the restaurant check: "))
if check_amount < 0:
    print("Error: Check amount cannot be negative.")
    exit(1)

tip_percentage = float(input("Enter the tip percentage: "))
if tip_percentage < 0:
    print("Error: Tip percentage cannot be negative.")
    exit(1)

number_of_diners = int(input("Enter the number of diners: "))
if number_of_diners < 0:
    print("Error: Number of diners cannot be negative.")
    exit(1)

# The program should output the total amount with tip, and the amount each diner owes.
total_amount = check_amount + (check_amount * tip_percentage / 100)
amount_per_diner = total_amount / number_of_diners

print(f"Total amount with tip: ${total_amount:.2f}")
print(f"Amount each diner owes: ${amount_per_diner:.2f}")
exit(0)
