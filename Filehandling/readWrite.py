#
#
# r+ (Read and Write):
#
# Opens the file for both reading and writing.
# Does not truncate the file; the file content remains unchanged.
# The file pointer is placed at the beginning of the file.
# if the file doesnot exits then it will raise an error


# Open the file in 'w' mode to write initial content
f = open('readWrite.txt', 'w')
f.write('Hello, I am Saiprabhu, currently in a learning bootcamp.')
f.close()

# Open the file in 'r+' mode to read and write
f = open('readWrite.txt', 'r+')

# Read the content
content = f.read()
print("The file contains:", content)

# Write additional content
f.write('\nLearning File Handling In python.........')
f.write('\nLearning File Handling In javaaaa.........')

# Move the file pointer to the beginning again for reading the modified content
f.seek(0)

# Read the modified content
modified_content = f.read()
print("The modified file contains:", modified_content)

# Close the file
f.close()


