x = True
y = False
result = x and y
print(result)  # False


x = True
y = False
result = x or y
print(result)  # True


x = True
result = not x
print(result)  # False


a = 5
b = 0
result = a and b
print(result)  # 0 (Falsy value of b)


result = 2.02 and 0.23
print(result)  # 0.23


result = 0.00 and 2.21
print(result)  # 0.0


result = 1.23 or 2.23
print(result)  # 1.23
