
# The seek() method in Python is used to change the current file position within a file.
# It allows you to move the file cursor to a specific position in the file.

# file.seek(offset, whence)


# offset: It represents the number of bytes to move the cursor. A positive value moves the cursor forward, and a negative value moves it backward.
#
# whence: It specifies the reference point for the offset. The possible values are:
#
# 0 (default): The beginning of the file.
# 1: The current file position.
# 2: The end of the file.

# Example 1: Move the cursor to the beginning of the file
file = open('example.txt', 'r')
file.seek(0)
content = file.read()
print(content)
file.close()

# Example 2: Move the cursor 10 bytes forward from the current position
file = open('example.txt', 'r')
file.seek(10, 0)
content = file.read()
print(content)
file.close()

