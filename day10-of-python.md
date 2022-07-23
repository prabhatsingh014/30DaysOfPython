# If Elif Else Statement in Python

- To execute statement based on a condition, python block (suite) "if" can be used.
```
if True:
    print("This is true")

if False:
    print("This is true")
```
- There could be multiple statements in a block.
- statements within an "if" block must be indented with the same number of spaces of tabs, otherwise, it won't be considered as part of the block. As mentioned in the below code sample, first print statement is part if block, whereas, second print statement is not.
```
if True:
    print("This is True")
print("Bye")
```
- if you'd like to execute statement based on some actual operations like arithmetic, then you can also use if block to compare such as an example of finding out even number
```
x = 8
res = x % 2
if res == 0:
    print("Even")
```
- If you'd like to execute the statement based on condition other than the one provided earlier, then you can also use another if statement
```
x = 8
res = x % 2
if res == 0:
    print("Even")
if res == 1:
    print("Odd")
```
- it's always recommended to improve the code efficiency. with the example using multiple if statements in a single program, all "if" statement will be examined even if it is not required, so to overcome that, we have "else" block
```
x = int(input("Enter a number: "))
res = x % 2
if res == 0:
    print("Even")
else:
    print("Odd")
```
- you can also use if inside an if statement, which is called nested if
```
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
```
- when there is a requirement to compare multiple condition, you can also make use of "elif" block which is nothing but "else-if" such as
```
x = int(input("Enter a number: "))

if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
# For all other cases, execute the else statement
else:
    print("Wrong input")
```
- for concatenation in print function, use "+" and then variable name e.g. print ("Greatest number is " + str1)
- for printing the integer value in the print function, use "," and the variable name e.g. print("Greater number is " , x)