# Break, Continue, Pass in Python
- break: jump out of the loop
```
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
```
- continue: skip the remaining steps in the loop and continue with next iteration
```
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
```
```
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)
```
- pass: there is no code, move to the next condition
```
for i in range(1,101):
    if i % 2 != 0:
        pass
    else:
        print(i)
```