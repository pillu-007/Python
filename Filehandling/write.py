

# Write Mode ('w'):
#
# This mode is used for writing or truncating the contents of a file.
# If the file does not exist, Python will create a new file.
# If the file already exists, it will truncate the file to zero length (erase its content) before writing.

# Write content to the file
file = open('write.txt', 'w')
file.write('Hello saiprabhu....')
file.close()

# Read the content of the file
file = open('write.txt', 'r')
content = file.read()
print("Content before append:", content)
file.close()

# Append additional content to the file
file = open('write.txt', 'a')
file.write('\nLearning File Handling In Python.....!')
file.close()

# Read the updated content of the file
file = open('write.txt', 'r')
content = file.read()
print("Content after append:", content)
file.close()

