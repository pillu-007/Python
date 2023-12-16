

# Iterates over a sequence (such as a list, tuple, string, or range) or other iterable objects.

# Example using a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example using a range
for i in range(5):  # prints 0 to n-1
    print(i, end=' ')

print()

for i in range(2,10):  # prints 2 to 9
    print(i, end=' ')

print()

for i in range(2, 10,2):
    print(i, end=' ')

print()

for i in range(10, 0,-1):
    print(i, end=' ')

print()

    # while loop
    # Continues to execute a block of code as long as a specified condition is True

count = 0
while count < 5:
    print(count, end=' ')
    count += 1


print()

for i in range(10):
    if i == 5:
        break
    print(i, end=' ')


# Transfer Statements

for i in range(10):
    if i == 5:
        break
    print(i, end=' ')

print()


for i in range(5):
    if i == 2:
        continue
    print(i, end=' ')

print()

for i in range(3):
    if i == 1:
        pass
    else:
        print(i, end=' ')

print()


# for-else loop
# In a for-else loop, the else block is executed when the loop has exhausted all the items in the iterable (list, tuple, string, etc.),
# i.e., when the loop completes normally (not interrupted by a break statement).

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "orange":
        print("Found orange!")
        break
else:
    print("Orange not found in the list.")

# while-else
# In a while-else loop, the else block is executed when the condition of the while loop becomes False (the loop completes normally).


count = 0

while count < 5:
    print(count,emd=' ')
    count += 1
else:
    print("Loop completed successfully.")


# del keyword
x = 42
print("Before using del:", x)

# Using del to delete the variable x
del x

# print("After using del:", x)
