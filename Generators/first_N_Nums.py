

def firstn(num):
    n = 1
    while n <= num:
        yield n
        n = n + 1

# Creating a generator object
values = firstn(5)

# Using the generator in a for loop
for x in values:
    print(x,end=' ')
