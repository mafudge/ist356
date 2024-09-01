colors = []

while True:
    color = input("Enter a color:")
    if color == 'quit':
        break
    if color not in colors:
        colors.append(color)
        op = "added to"
    else:
        op = "already in"

    print(f"{color} {op} {colors}")