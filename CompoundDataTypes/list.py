# list data type
# if we want to represent a group of objects as a single entity , then we can go for list
# list are mutable , insertion order is preserved , indexing and slicing is possible , represented using []
# duplicates are allowed

# Creating a list
my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 4, 5]

# Getting the id of each list
id_of_my_list = id(my_list)
id_of_my_list2 = id(my_list2)


# Getting the id of one element from each list
id_of_first_element_in_my_list = id(my_list[0])
id_of_first_element_in_my_list2 = id(my_list2[0])

# Printing the results
print("ID of my_list:", id_of_my_list)
print("ID of my_list2:", id_of_my_list2)
print("ID of the first element in my_list:", id_of_first_element_in_my_list)
print("ID of the first element in my_list2:", id_of_first_element_in_my_list2)

# Printing the original list
print("Original List:", my_list)

# Appending an element to the end of the list
print("ID of my_list after appending 6: ", id_of_my_list)


my_list.append(6)
print("List after appending 6:", my_list)


#After appending checking the id of my_list

# Inserting an element at a specific position
my_list.insert(2, 10)
print("List after inserting 10 at index 2:", my_list)

# Removing an element by value
my_list.remove(3)
print("List after removing the element 3:", my_list)


# Removing an element by index
removed_element = my_list.pop(1)
print("List after popping element at index 1:", my_list)
print("Removed element:", removed_element)

# Extending the list with another list
extension_list = [7, 8, 9]
my_list.extend(extension_list)
print("List after extending with [7, 8, 9]:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed List:", my_list)

# Sorting the list
my_list.sort()
print("Sorted List:", my_list)

# Finding the minimum and maximum values in the now-empty list
# Note: This will raise a ValueError since the list is empty
min_value = min(my_list)
max_value = max(my_list)

# Accessing the first element of the sorted list
first_element = my_list[0]
print(first_element)

# Accessing the last element using negative indexing
last_element = my_list[-1]
print("Last Element:", last_element)

# Accessing a sublist from the end (last 3 elements) using negative slicing
last_three_elements = my_list[-3:]
print("Last Three Elements:", last_three_elements)

# Extracting a sublist from index 1 to 3 (exclusive)
sublist = my_list[1:4]
print(sublist)

# Finding the index of the value 4 in the list
index_of_4 = my_list.index(4)
print(index_of_4)



# Clearing all elements from the list
my_list.clear()
print(my_list)

# Creating a shallow copy of the now-empty list
new_list = my_list.copy()
print(new_list)

# Getting the length (number of elements) of the list
length_of_list = len(my_list)
print(length_of_list)

#Nested list
nested_list = [1,2,3,[4,5,6],7,8,9]

# Accessing the third element of the nested list
print(nested_list[2])

# Accessing the second element of the inner list
print(nested_list[3][1])

# Modifying the first element of the inner list
nested_list[3][0] = 99
print(nested_list)

# Adding an element to the end of the inner list
nested_list[3].append(10)
print(nested_list)

# Removing the second element of the outer list
nested_list.pop(1)
print(nested_list)


my_list = [1, "hello", (2, 3), 4.5]

# Accessing elements in the list
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[2][0])
print(my_list[2][1])
print(my_list[3])


b=[1,2,3,4,5,6,-7,-9,-2]

a=[x for x in b if x%2==0 and x>0 ]

a = lambda x: x%2==0 and x>0