PASSWORD = "secret"

for attempt in range(5):
    entered_password = input("Enter the password: ")
    if PASSWORD == entered_password:
        print("Access granted")
        break
    else:
        print("Access denied")
        
    print(f"Attempt {attempt + 1} of 5")

if not success:
    print("You are locked out")

