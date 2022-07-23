# While loop in python

- for repetitive tasks, we use loop in python
- one loop type is called while which will run until the condition stands incorrect
- there are 3 parts in a loop: initialize, condition, increment/decrement
- first you have to initialize to start compare from some point, then execute the condition and then increment/decrement
```
i = 1
while i <= 5:
    print("Hello World")
    i = i + 1
```
- you can also use nested while loop i.e. while loop inside a while loop
```
i = 1
while i <= 5:
    j = 1
    print("Hello World", end=" ")
    while j <= 4:
        print("!", end=" ")
        j = j + 1
    i = i + 1
    print()
```