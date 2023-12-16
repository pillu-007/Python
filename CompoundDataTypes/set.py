# set datatype
# if we want to represent a group of objects as a single entity  without duplication and insertion order is not required then we can go for
# set datatype
# indexing and slicing are not allowed here and set is mutable


# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2, 3, 4, 5}

# Getting the id of each set
id_of_set1 = id(set1)
id_of_set2 = id(set2)
id_of_set3 = id(set3)

# Printing the results
print("ID of set1:", id_of_set1)
print("ID of set2:", id_of_set2)
print("ID of set3:", id_of_set3)


# Printing the original sets
print("Set 1:", set1)
print("Set 2:", set2)

# Adding an element to a set
set1.add(6)
print("Set 1 after adding 6:", set1)
print("ID of set1 after adding 6:", id(set1))

# Removing an element from a set
set1.remove(3)
print("Set 1 after removing 3:", set1)
print("ID of set1 after removing 3:", id(set1))


# Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
popped_element = set1.pop()
print("Popped element from Set 1:", popped_element)

# Creates a shallow copy of the set.
copied_set = set1.copy()
print("Shallow copy of Set 1:", copied_set)

# Creates a new set by applying an expression to each item in an iterable.
square_set = {x**2 for x in set1}
print("Set of squares from Set 1:", square_set)


# Creates an immutable version of a set, known as a frozen set.
frozen_set = frozenset(set1)
print("Frozen Set from Set 1:", frozen_set)

# Union of two sets
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)

# Intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Difference between two sets
difference_set = set1.difference(set2)
print("Difference between Set 1 and Set 2:", difference_set)

# Checking if one set is a subset of another
is_subset = set1.issubset(set2)
print("Is Set 1 a subset of Set 2:", is_subset)

# Checking if two sets are disjoint
is_disjoint = set1.isdisjoint(set2)
print("Are Set 1 and Set 2 disjoint:", is_disjoint)

# Clearing all elements from a set
set1.clear()
print("Set 1 after clearing:", set1)


