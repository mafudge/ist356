pos = 0
neg = 0

while True:
    num = int(input("Enter an integer:"))
    if num > 0:
        pos = pos + 1
    elif num < 0:
        neg = neg + 1
    else:
        break

print(f"Number of + numbers entered: {pos}")
print(f"Number of - numbers entered: {neg}")
