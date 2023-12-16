#dictionaries
# dictionaries are used to store key value pairs and are mutable , insertion order is preserved

# Creating a dictionary
my_dict = {'name': 'saiprabhu', 'age': 22, 'city': 'Adilabad'}
print("id of my_dict dictionary",id(my_dict))

# Displaying the original dictionary
print("Original Dictionary:", my_dict)

# Accessing values
print("Name:", my_dict['name'])

# Updating values
my_dict['age'] = 31
print("Updated Age:", my_dict['age'])
print("id of my_dict dictionary after updation",id(my_dict))

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print("Updated Dictionary:", my_dict)

# Removing a key-value pair
removed_value = my_dict.pop('city')
print("Removed City:", removed_value)
print("Updated Dictionary:", my_dict)

# Iterating through keys
print("Keys:")
for key in my_dict.keys():
    print(key)

# Iterating through values
print("Values:")
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
print("Key-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key is present
print("Is 'age' present?", 'age' in my_dict)

# Getting a default value for a key
print("Salary:", my_dict.get('salary', 'Not Available'))

# Clearing all elements from the dictionary
my_dict.clear()
print("Cleared Dictionary:", my_dict)

my_dict = {'name': 'saiprabhu', 'age': 22, 'city': 'Adilabad'}

# Dictionary comprehension with a condition
string_values_dict = {key: value for key, value in my_dict.items() if isinstance(value, str)}

print(string_values_dict)
