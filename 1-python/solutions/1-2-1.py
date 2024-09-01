valid_password = "secret"
for i in range(5):
    pw = input("Enter Password:")
    if pw == valid_password:
        print("Access Granted!")
        break
    else:
        print("Invalid Password.")
else:
    print("You are locked out")