# Key shortcuts in IDLE for Python

- IDLE -> Options -> Configure IDLE -> Keys -> Select operation to configure -> Get New Keys for Selection -> Select new key -> OK

# Bitwise Operator

- Compliment (~)
- Bitwise AND (&)
- Bitwise OR (|)
- Bitwise XOR (^)
- Leftshift (<<)
- Rightshift (>>)

```
>>> ~12
-13
>>> 12 & 13
12
>>> 12 | 13
13
>>> 12 ^ 13
1
>>> 12 << 2
48
>>> 12 >> 2
3
>>> 
```

# Import Math Fuction in Python

```
>>> import math
>>> print(math.sqrt(25))
5.0
>>> print(math.pow(2,2))
4.0
>>> 
>>> import math as m
>>> print(m.sqrt(25))
5.0
>>> print(m.pow(2,3))
8.0
>>> 
>>> from math import sqrt, pow
>>> print(math.sqrt(25))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(math.sqrt(25))
NameError: name 'math' is not defined
>>> print(sqrt(25))
5.0
>>> print(pow(3,2))
9.0
>>> 
```
