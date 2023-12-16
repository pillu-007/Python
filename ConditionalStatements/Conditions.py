x = 10
if x > 5:
    print("x is greater than 5")

# if-else
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

#if-elif-if
x = 3
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


# nested if-else
x = 10
if x > 5:
    if x % 2 == 0:
        print("x is greater than 5 and even")
    else:
        print("x is greater than 5 but odd")


#ternary operator
x = 7
result = "Even" if x % 2 == 0 else "Odd"
print(result)


# Nested ternary operator
x = 10
result = "Even" if x % 2 == 0 else ("Positive" if x > 0 else "Negative")
print(result)
