
# Read Mode ('r'):
#
# This mode is used for reading the contents of a file.
# If the file does not exist, it will raise a FileNotFoundError.
# The file pointer is positioned at the beginning of the file.

# Read Mode ('r'):

# Open the file in read mode
file = open('write.txt', 'r')

# Read the entire content of the file
content = file.read()
print("Content before append:", content)

# Move the file pointer to the beginning for further operations
file.seek(0)

# Read the file line by line
print("\nReading the file line by line:")
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()


# Move the file pointer to the beginning for further operations
file.seek(0)

print(file.readlines())  # will stores all the lines in form of a list.....
# Close the file
file.close()


# if we use with keyword when opening a file we dont need to explicitly close the file , it automatically close...