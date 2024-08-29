bill = float(input("Enter the total amount of the bill $"))
tip = int(input("What % would you like to tip, eg. 20 == 20%? "))
tip_pct = tip/100
diners = int(input("How many diners? "))
total = bill + bill*tip_pct
share = total / diners
print("Total Bill, with Tip: ", total)
print(f"Even share among {diners} diners is {share:.2f}")