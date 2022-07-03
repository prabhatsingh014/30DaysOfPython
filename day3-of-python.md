# Comparison Operators

- In python, we can use 6 comparison operators
- == equal to, != not equal to, < less than, <= less than or equal to, > greater than, >= greater than or equal to

```
>>> 'python'>'Python'
True
>>> 'python'<'Python'
False
>>> x = 6
>>> y = 7
>>> print(x != y)
True
>>> min_score = 13
>>> score = 13
>>> print(score > min_score)
False
>>> print(score <= min_score)
True
>>> a = [10, 20]
>>> b = a
>>> b += [30, 40]
>>> print(a)
[10, 20, 30, 40]
>>> print(b)
[10, 20, 30, 40]
>>> 
>>> print(2<4)
True
>>> y = 20
>>> x = y += 3
  File "<stdin>", line 1
    x = y += 3
          ^^
SyntaxError: invalid syntax
>>>
```

# Condition statement: 
```
if <condition>: 
```
OR
```
if <condition>:
  print(<statement>)
else:
  print(<statement>)
```
OR
```
if <condition>:
  print(<statement>)
elif <condition>:
  print(<statement>)
else:
  print(<statement>)
```
OR
```
if <condition>:
 if <condition>:
   print(<statement>)
 else:
   print(<statement>)

```

```
prabhat>> cat if-else-1.py 
if 4 + 5 == 10:
  print("True")
else:
  print("False")
print("True")
prabhat>> python3 if-else-1.py 
False
True
prabhat>> 
prabhat>> cat if-else-2.py 
a = 5
b = 10

if b > a:
print("b is greater than a")
prabhat>> 
prabhat>> python3 if-else-2.py 
  File "/Users/dawn/if-else-2.py", line 5
    print("b is greater than a")
    ^
IndentationError: expected an indented block after 'if' statement on line 4
prabhat>> 
prabhat>> cat if-else-3.py 
if (5,10): print('hello')
prabhat>> python3 if-else-3.py 
hello
prabhat>> 
prabhat>> cat if-else-4.py 
if (yes): print('hello')
prabhat>> 
prabhat>> python3 if-else-4.py 
Traceback (most recent call last):
  File "/Users/dawn/if-else-4.py", line 1, in <module>
    if (yes): print('hello')
NameError: name 'yes' is not defined
prabhat>> 
prabhat>> cat if-else-5.py 
if True: print('hello')
prabhat>> 
prabhat>> python3 if-else-5.py 
hello
prabhat>> 
prabhat>> cat if-else-6.py 
if (5,10):
print('hello')
prabhat>> 
prabhat>> python3 if-else-6.py 
  File "/Users/dawn/if-else-6.py", line 2
    print('hello')
    ^
IndentationError: expected an indented block after 'if' statement on line 1
prabhat>> 
prabhat>> cat if-else-7.py 
x = -10
if x < 0:
  print("The negative number ", x, "is not valid here.")
print("This is always printed")
prabhat>> 
prabhat>> python3 if-else-7.py 
The negative number  -10 is not valid here.
This is always printed
prabhat>> 
prabhat>> cat if-else-8.py 
x = 3
if ( x == 0 ):
  print("Am I here?")
elif ( x == 3 ):
  print("Or here?")
print("Or over here?")
prabhat>> 
prabhat>> python3 if-else-8.py 
Or here?
Or over here?
prabhat>> 
prabhat>> cat if-else-9.py 
x = 0
a = 6
b = 6
if a > 0:
    if b < 0: 
        x = x + 6 
    elif a > 6:
        x = x + 5
    else:
        x = x + 4
else:
    x = x + 3

print(x)
prabhat>> 
prabhat>> python3 if-else-9.py 
4
prabhat>> 
prabhat>> cat if-else-10.py 
a = 5
b = 10
if b < a:
  print("a is greater than b")
elif a == b:
  b = 5
  print("a and b are equal")
else:
  print("b is greater than a")
prabhat>> 
prabhat>> python3 if-else-10.py 
b is greater than a
prabhat>> 
```

# Loop - While
- While loop runs a statement until the condition is true. Once it's false, it stops.
- While loop also includes an else statement to run the statement in case the condition is no longer true.

```
prabhat>> cat while-loop-1.py 
x = 0
while (x < 50):
  x+=2

print(x)
prabhat>> python3 while-loop-1.py 
50
prabhat>> 
prabhat>> cat while-loop-2.py 
i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1
prabhat>> 
prabhat>> python3 while-loop-2.py 
1
2
prabhat>> 
prabhat>> cat while-loop-3.py 
i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2
prabhat>> 
prabhat>> python3 while-loop-3.py 
2
4
prabhat>> 
prabhat>> cat while-loop-4.py 
x = 1
while ( x < 20 ):
 x = x * 2
print(x)
prabhat>> 
prabhat>> python3 while-loop-4.py 
32
prabhat>> 
prabhat>> cat while-loop-5.py 
i = 1
x = 3
sum = 0
while ( i <= x ):
 sum += i
 i += 1
print(sum)
prabhat>> 
prabhat>> python3 while-loop-5.py 
6
prabhat>> 
prabhat>> cat while-loop-6.py 
i = 5
while True:
    if i % 0o11 == 0:
        break
    print(i)
    i += 1
prabhat>> 
prabhat>> python3 while-loop-6.py 
5
6
7
8
prabhat>> 
prabhat>> cat while-loop-7.py 
i = 1
while True:
    if i % 0o7 == 0:
        break
    print(i)
    i += 1
prabhat>> 
prabhat>> python3 while-loop-7.py 
1
2
3
4
5
6
prabhat>> 
prabhat>> cat while-loop-8.py 
x = 1
while ( x <= 5 ):
  x += 1
print(x)
prabhat>> 
prabhat>> python3 while-loop-8.py 
6
prabhat>> 
```

# Loop - For

- For loop: run a condition within a range
- You can also break out from a loop based on a condition using if <condition>: break
- Or you can also skip a value from a loop based on a condition using if <condition>: continue
- For defining range, range() fuction is used e.g. range(5) which means 0,1,2,3,4
- To start range from a specific value, you can also define the starting value in the range() function such as range(2,5) which means 2,3,4

```
prabhat>> cat for-loop-1.py 
x = 'abcd'
for i in x:
    print(i.upper())
prabhat>> python3 for-loop-1.py 
A
B
C
D
prabhat>> 
prabhat>> 
prabhat>> cat for-loop-2.py 
x = 'abcd'
for i in range(x):
    print(i)
prabhat>> python3 for-loop-2.py 
Traceback (most recent call last):
  File "/Users/dawn/for-loop-2.py", line 2, in <module>
    for i in range(x):
TypeError: 'str' object cannot be interpreted as an integer
prabhat>> 
prabhat>> 
prabhat>> cat for-loop-3.py 
for num in range(0, 11):
  if num%2 != 0:
    print(num);
print(num)
prabhat>> python3 for-loop-3.py 
1
3
5
7
9
10
prabhat>> 
prabhat>> 
prabhat>> 
prabhat>> cat for-loop-4.py 
x = 'abcd'
for i in range(len(x)):
    print("hello")
prabhat>> python3 for-loop-4.py 
hello
hello
hello
hello
prabhat>> 
prabhat>> 
prabhat>> 
prabhat>> cat for-loop-5.py 
x = 'abcd'
for i in x:
    print(i)
    x.upper()
prabhat>> python3 for-loop-5.py 
a
b
c
d
prabhat>> 
prabhat>> 
prabhat>> 
prabhat>> cat for-loop-6.py 
x = 'abcd'
for i in range(len(x)):
    i.upper()
print (x)
prabhat>> python3 for-loop-6.py 
Traceback (most recent call last):
  File "/Users/dawn/for-loop-6.py", line 3, in <module>
    i.upper()
AttributeError: 'int' object has no attribute 'upper'
prabhat>> 
prabhat>> 
prabhat>> 
prabhat>> cat for-loop-7.py 
x = 'abcd'
for num in range(5, 11):
  print(num)
prabhat>> python3 for-loop-7.py 
5
6
7
8
9
10
prabhat>> 
prabhat>> 
prabhat>> 
prabhat>> cat for-loop-8.py 
x = 2021
for i in x:
  print(i)
prabhat>> python3 for-loop-8.py 
Traceback (most recent call last):
  File "/Users/dawn/for-loop-8.py", line 2, in <module>
    for i in x:
TypeError: 'int' object is not iterable
prabhat>> 
prabhat>> 
prabhat>> 
prabhat>> cat for-loop-9.py 
x = 'abcd'
for i in range(len(x)):
    print(i)
prabhat>> python3 for-loop-9.py 
0
1
2
3
```
