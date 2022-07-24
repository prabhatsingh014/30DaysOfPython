# For loop in python
- similary to while loop, for loop is also used for repetitive tasks
- different from while loop in the sense that it doesn't required to be initialized such as
```
x = ["prabhat",65,2.5]
for i in x:
    print(i)
```
- with for loop, you can use list, tuple, set as given above for the list
- you can also use the list, tuple, or set directly in the for loop instead of defining it in a variable such as:
```
for i in ["prabhat", 65, 2.5]
    print(i)
```
- you can also use for loop with a string type variable such as
```
x = 'PRABHAT'
for i in x:
    print(i)
```
- you can also use range function in the for loop to execute the task certain number of times such as
```
for i in range(10):
    print(i)
```
- range(10) means the value from 0 to 9
- range fuction takes three values i.e. starting, ending, and interval such as
```
for i in range(11,21,1):
    print(i)
```
```
# for reverse counting
for in in range(20,10,-1)
    print(i)
```
- you can also use conditional statement within for loop.
```
for i in (1,21,1):
    if i % 5 != 0:
        print(i)
```
- you can also use nested for loop meaning for loop within for loop