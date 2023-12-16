

def countdown(num):
    print("Start Countdown")
    while num > 0:
        yield num
        num = num - 1

values = countdown(5)
for x in values:
    print(x)
