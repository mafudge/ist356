grocery_list = []
while True:
    grocery_item = input("Enter grocery item (or 'done' to finish): ")
    if grocery_item.lower() == 'done':
        break
    quantity = int(input(f"Enter quantity for {grocery_item}: "))
    grocery_list.append({'item': grocery_item, 'quantity': quantity})
    print(f"Added {quantity} of {grocery_item} to the list.")

print(grocery_list)

