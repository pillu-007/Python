

# Append Mode ('a'):
#
# This mode is used for appending data to the end of a file.
# If the file does not exist, Python will create a new file.
# The file pointer is positioned at the end of the file.

# Append additional content to the file
file = open('append.txt', 'a')
file.write('\nLearning File Handling In Python.........!')
file.close()

# Open the file in read mode
file = open('append.txt', 'r')

# Read the entire content of the file
content = file.read()
print("\nContent after append:", content)

# Move the file pointer to the beginning for further operations
file.seek(0)

# Read the file line by line
print("\nReading the file line by line:")
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()

# Close the file
file.close()
