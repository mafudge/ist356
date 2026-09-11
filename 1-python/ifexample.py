#Elif versus multiple ifs...
# One decision or multiple decisions. 

x = int(input("enter an integer"))

# one decision
if x>10:
    print("A:bigger than 10")
elif x>20:
    print("A:bigger than 20")    

    # Multiple decisions
if x>10:
    print("B:bigger than 10")
if x>20:
    print("B:bigger than 20")