

# Write and Read Mode ('w+'):
#
# This mode is used for both reading and writing to a file.
# If the file does not exist, Python will create a new file.
# If the file already exists, it will truncate the file to zero length before writing.
# The file pointer is positioned at the beginning of the file.


f = open('writeRead.txt', 'w+')

# f.write('Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.')
print(f.read())
f.seek(0)

content = f.read()
print(content)
f.close()
