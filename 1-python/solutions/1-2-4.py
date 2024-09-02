items = {}

while True:
    item = input("Enter shopping item, or 'quit': ")
    if item == 'quit':
        break
    qty = int(input("Enter quantity: "))
    if item in items.keys():
        items[item] = items[item] + qty
    else:
        items[item] = qty

    print("ITEMS:", items)