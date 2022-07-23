x = int(input("Enter a number: "))
res = x % 2
if res == 0:
    print("Even")
    if x > 5:
        print("Great")
    else:
        print("Not so great")
else:
    print("Odd")