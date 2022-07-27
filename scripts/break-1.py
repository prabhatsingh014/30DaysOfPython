candy = int(input("How many candies do you want? "))

available = 5
i = 1

while i <= candy:
    if i > available:
        print("Out of stock")
        break
    print("Candy")
    i += 1

print("Bye")