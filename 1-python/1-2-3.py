# write a sentiel controlled loop to input a color until quit
# add the color to a list and print the list each time
# do not add a color if its already in the list
# keep a separate list of duplicate colors and print it at the end
colors = []
duplicates = []
while True:
    color = input("Enter a color (or 'quit' to exit): ")
    if color.lower() == 'quit':
        break
    if color not in colors:
        colors.append(color)
    else:
        duplicates.append(color)
    print(f"Current list: {colors}")

print(f"Duplicate colors: {duplicates}")
red