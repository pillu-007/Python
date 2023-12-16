# Multi-line statement with \ , (), [], and {}
numbers = [1, 2, 3,
           4, 5, 6]

result = (
    sum(numbers) +
    len(numbers) -
    min(numbers)
)


total = 1+2+ \
    3+4+ \
    5+7+8

print("total",total)
if (
    result % 2 == 0 and
    result > 0
):
    print(f"The result is a positive even number: {result}")
else:
    print(f"The result is not a positive even number: {result}")
