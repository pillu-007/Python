# Tuple data type
# If we want to represent an immutable group of objects as a single entity, then we can go for a tuple
# Tuples are immutable, insertion order is preserved, indexing and slicing are possible, represented using ()
# duplicates are allowed


# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
my_tuple2 = (1, 2, 3, 4, 5)

# Getting the id of each tuple
id_of_my_tuple = id(my_tuple)
id_of_my_tuple2 = id(my_tuple2)

# Getting the id of one element from each tuple
id_of_first_element_in_my_tuple = id(my_tuple[0])
id_of_first_element_in_my_tuple2 = id(my_tuple2[0])

# Printing the results
print("ID of my_tuple:", id_of_my_tuple)
print("ID of my_tuple2:", id_of_my_tuple2)
print("ID of the first element in my_tuple:", id_of_first_element_in_my_tuple)
print("ID of the first element in my_tuple2:", id_of_first_element_in_my_tuple2)

# Printing the original tuple
print("Original Tuple:", my_tuple)

# Tuple operations (Note: Tuples are immutable, so methods that modify the tuple are not available)
# Indexing, slicing, and other non-modifying operations can be performed.

# Accessing the first element of the tuple
first_element = my_tuple[0]
print(first_element)

# Accessing the last element using negative indexing
last_element = my_tuple[-1]
print("Last Element:", last_element)

# Accessing a sublist from index 1 to 3 (exclusive)
subtuple = my_tuple[1:4]
print(subtuple)

# Finding the index of the value 4 in the tuple
index_of_4 = my_tuple.index(4)
print(index_of_4)

# Getting the length (number of elements) of the tuple
length_of_tuple = len(my_tuple)
print(length_of_tuple)

# nested tuple
nested_tuple = (1, "hello", (2, 3), 4.5)


print(nested_tuple[0])
print(nested_tuple[1])
print(nested_tuple[2])
print(nested_tuple[2][0])
print(nested_tuple[2][1])
print(nested_tuple[3])


# list in tuple
my_tuple = (1, "hello", [2, 3], 4.5)
my_tuple[2][0] = 99
# Displaying the modified tuple
print(my_tuple)
