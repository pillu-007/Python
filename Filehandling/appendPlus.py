#
#
# Append and Read Mode ('a+'):
#
# This mode is used for both reading and appending to a file.
# If the file does not exist, Python will create a new file.
# The file pointer is positioned at the end of the file.


f = open('appendPlus.txt', 'a+')
f.write('\nHello i am a+ mode......')
f.seek(0)
content = f.read()
print(content)

f.write('\nhello i am prabhu....')
f.close()
