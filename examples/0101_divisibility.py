x = 10

if x % 2 == 0:
    if x % 3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Divisble only by 2")
elif x % 3 == 0:
    print("Divisible only by 3")
else:
    print("Not divible by 3 and 2")