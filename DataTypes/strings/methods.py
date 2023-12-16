# strings and its methods

# String, lstrip, and rstrip program

# Original string with leading and trailing whitespaces
original_string = "   Python Programming   "

# Using strip() to remove leading and trailing whitespaces
stripped_string = original_string.strip()

# Using lstrip() to remove leading whitespaces
left_stripped_string = original_string.lstrip()

# Using rstrip() to remove trailing whitespaces
right_stripped_string = original_string.rstrip()

# Printing the results
print("Original String:", original_string)
print("Stripped String:", stripped_string)
print("Left Stripped String:", left_stripped_string)
print("Right Stripped String:", right_stripped_string)

# Split method program

# Original string with spaces
sentence = "Python is a versatile programming language"

# Using split() to split the string into a list of words
word_list = sentence.split()

# Using split() with a specific delimiter (comma)
csv_data = "John,Doe,30,Engineer"
csv_list = csv_data.split(',')

# Using split() with a specific delimiter (hyphen)
date_string = "2022-12-01"
date_list = date_string.split('-')

# Printing the results
print("Original Sentence:", sentence)
print("Word List:", word_list)

print("\nUsing split() with a specific delimiter:")
print("CSV Data:", csv_data)
print("CSV List:", csv_list)

print("Date String:", date_string)
print("Date List:", date_list)


print()


# Join method program

# List of words
word_list = ["Python", "is", "a", "versatile", "programming", "language"]

# Using join() to concatenate list elements into a string
joined_sentence = ' '.join(word_list)

# Tuple of characters
char_tuple = ('H', 'e', 'l', 'l', 'o')

# Using join() to concatenate tuple elements into a string
joined_string = ''.join(char_tuple)

# Set of words
word_set = {"This", "is", "a", "set", "of", "words"}

# Using join() to concatenate set elements into a string
joined_set = ' '.join(word_set)

# Printing the results
print("List of Words:", word_list)
print("Joined Sentence:", joined_sentence)

print("\nTuple of Characters:", char_tuple)
print("Joined String:", joined_string)

print("\nSet of Words:", word_set)
print("Joined Set:", joined_set)

print()

# Replace method program

# Original string
original_string = "Python is a versatile programming language. Python is widely used."

# Using replace() to replace a substring
replaced_string = original_string.replace("Python", "Java")

# Using replace() to replace multiple occurrences
multi_replace_string = original_string.replace("Python", "Java", 1)

# Printing the results
print("Original String:", original_string)

print("\nUsing replace() to replace a substring:")
print("Replaced String:", replaced_string)

print("\nUsing replace() to replace multiple occurrences:")
print("Multi-Replaced String:", multi_replace_string)

# String methods: upper(), lower(), capitalize(), isupper(), islower()

# Original string
text = "python programming"

# Using upper() to convert the string to uppercase
uppercase_text = text.upper()

# Using lower() to convert the string to lowercase
lowercase_text = text.lower()

# Using capitalize() to capitalize the first letter of the string
capitalized_text = text.capitalize()

# Using isupper() to check if the string is in uppercase
is_upper = text.isupper()

# Using islower() to check if the string is in lowercase
is_lower = text.islower()

# Printing the results
print("Original Text:", text)
print("\nUsing upper():", uppercase_text)
print("Using lower():", lowercase_text)
print("Using capitalize():", capitalized_text)

print("\nUsing isupper():", is_upper)
print("Using islower():", is_lower)

# String methods: isalpha(), isdigit(), isalnum()

# Original strings
alpha_string = "Python"
digit_string = "12345"
alnum_string = "Python123"

# Using isalpha() to check if the string consists of alphabetic characters only
is_alpha = alpha_string.isalpha()

# Using isdigit() to check if the string consists of numeric characters only
is_digit = digit_string.isdigit()

# Using isalnum() to check if the string consists of alphanumeric characters only
is_alnum = alnum_string.isalnum()

# Printing the results
print("Original Strings:")
print("isalpha():", is_alpha)
print("isdigit():", is_digit)
print("isalnum():", is_alnum)


# String methods: count(), find(), rfind()

# Original string
sentence = "Python is a powerful programming language. Python is widely used."

# Using count() to count the occurrences of a substring
count_python = sentence.count("Python")

# Using find() to find the index of the first occurrence of a substring
index_python = sentence.find("Python")

# Using rfind() to find the index of the last occurrence of a substring
last_index_python = sentence.rfind("Python")

# Printing the results
print("Original Sentence:", sentence)
print("\ncount('Python'):", count_python)
print("find('Python'):", index_python)
print("rfind('Python'):", last_index_python)

