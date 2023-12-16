import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python commandLine.py <number1> <number2>")
    sys.exit(1)

# Extract command-line arguments
number1 = float(sys.argv[1])
number2 = float(sys.argv[2])

# Calculate the sum
result = number1 + number2

# Print the result
print("The sum of two numbers is: ", result)
