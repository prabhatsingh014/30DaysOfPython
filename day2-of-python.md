## Variables

- Variable cannot start with numericals.
- Variable can only start with character (small or capital) or underscore).
- Reserved keywords cannot be used as variables.
- Reserved keywords can be used as variable with different case (e.g. import as Import).
- Variables can be operated upon using short operator such as: cost = cost + 2 is equivalent to cost += 2. Here "+=" is the short operator.
- Short operator works with other mathematical operations as well.
- Variable can containe number, just not at the start.
- It's not necessary to declare a variable first before assigning any value to the variable.

```
>>> age = 22
>>> AGE = 44
>>> age /= 2
>>> print(age + AGE)
55.0 
>>> amount = 4
>>> cost = 2
>>> cost += 2
>>> print(amount * cost)
16
>>> y = 5
>>> y = "Jack"
>>> print(y)
Jack
>>> 
```

## Comments

- Some additional information about your code
- Starts with hash '#'
- Multiple line comments should also have '#' in each line, otherwise, python will try to run it as code and result into syntax error.

```
>>> name = "Sally" # employee name
>>> data = "#123"
>>> print(name+data)
Sally#123
>>> 
>>> #x=5
>>> #y=6
>>> z=7
>>> print(x+y+z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> 
>>> #print("Hello, jack!")
>>> print("Hello, Sally!")
Hello, Sally!
>>> 
>>> print("line1")
line1
>>> #print("line2")
>>> print("#line3")
#line3
```

## Inputs

- Input function allows user to provide an input on the console.
- By default, all input function returns the string value.
- If the value returned by an input function is numeric in nature, it cannot be used for arithmetic operations as it is still a string.
- To treat the value as an integer and float number, typecast is used.
- Program that doesn't use any input function is known as a deaf program.

```
>>> print(int(15.5)-10)
5
>>> inputString = input('Enter a string: ')
Enter a string: Hello Python
>>> print(inputString, sep='#', end='&')
Hello Python&>>> 
>>> 
>>> inputString = input('Enter a string: ')
Enter a string: "Hello Python"
>>> print(inputString, sep='#', end='&')
"Hello Python"&>>> 
>>> 
>>> inputString = input('Enter a string: ')
Enter a string: HelloPython
>>> print(inputString*2)
HelloPythonHelloPython
>>> 
>>> age=input("My age is: ")
My age is: 25
>>> print(age)
25
>>> year_of_birth = int(input("In what year were you born? "))
In what year were you born? 1986
>>> print("You were born in " + ...(year_of_birth))
<stdin>:1: SyntaxWarning: 'ellipsis' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'ellipsis' object is not callable
>>> 
>>> print("You were born in " + year_of_birth)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 
>>> 
>>> print("You were born in " + ...(year_of_birth))
<stdin>:1: SyntaxWarning: 'ellipsis' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'ellipsis' object is not callable
>>> 
>>> 
>>> 
>>> year_of_birth = str(input("In what year were you born? "))
In what year were you born? 1986
>>> print("You were born in " + ...(year_of_birth))
<stdin>:1: SyntaxWarning: 'ellipsis' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'ellipsis' object is not callable
>>> print("You were born in " + ...(year_of_birth))
<stdin>:1: SyntaxWarning: 'ellipsis' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'ellipsis' object is not callable
>>> 
```

## String Methods

- We can use + operator in order to concatenate two strings
- We can use * operator in order to repeat certain strings certain amount of time
- When we multiple by 0 or negative number (-), it returns zero or empty string
- We can use str function in order to turn integers into string

```
>>> print("ha"*2)
haha
>>> Num = input("Enter a number: ")
Enter a number: 5
>>> Num = int(Num)
>>> print(Num*3)
15
>>> x = 5
>>> y = "Sally"
>>> print(str(x) + y)
5Sally
>>> 
>>> Num = input("Enter a Number: ")
Enter a Number: 5
>>> print(Num * 3)
555
```
