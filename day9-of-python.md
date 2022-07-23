# User input in python
- input function to use input values at the prompt
```
x = input()
y = input()
z = x + y
print(z)
```
- input function always give the value of type string by default
```
x = input("Enter first number: ")
print(type(x))
y = input("Enter second number: ")
print(type(y))
z = x + y

print(z)
print(type(z))
```
- if perform operation on different type of user input, then need to specify the relevant funtion e.g. int, float etc.
```
x = int(input("Enter first number: "))
print(type(x))
y = int(input("Enter second number: "))
print(type(y))
z = x + y
print(z)
print(type(z))
```
- with input function (str), you can use the index number to fetch a particular character e.g. input("enter a string")[0]
```
ch = input("Enter a character: ")
print(ch)

ch = input("Enter a character: ")
print(ch[0])

ch = input("Enter a character: ")[-1]
print(ch)
```
- to evaulate arithmetic expression, python also have a function called "eval" which can be used to solve an arithmetic expression in one line e.g. eval(input("enter an expression: ")) --> 2 + 6 - 1
```
res = eval(input("Enter an expression: "))
print(res)
```
- if you'd like to pass the value from the command line instead of defining in the script, you'd have to use the fuction "argv"
- argv function works with the index numbers, like 0 for python script name, 1 for first input, 2 for second input
- argv function is not loaded by default, you'd have to import sys module
```
import sys as s

x = s.argv[1]
y = s.argv[2]
z = x + y
print(z)
```
- argv function, like input function, gives the value of str type by default, so in order to work with other type inputs such as int, or float, you'd have to use the respective function
```
import sys as s

x = int(s.argv[1])
y = int(s.argv[2])
z = x + y
print(z)
```