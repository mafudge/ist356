import sys

# Check if we have exactly 3 arguments (program name + 3 numbers)
if len(sys.argv) != 4:
    print("Usage: python add_numbers.py <num1> <num2> <num3>")
    sys.exit(1)

try:
    # Convert command line arguments to numbers (float to handle decimals)
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    num3 = float(sys.argv[3])
    
    # Add the three numbers
    total = num1 + num2 + num3
    
    # Display the result
    print(f"{num1} + {num2} + {num3} = {total}")
except ValueError:
    print("Error: All arguments must be valid numbers")
    sys.exit(1)
