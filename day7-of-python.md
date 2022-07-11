# Operators

- Arithmetic Operators: +, -, /, %, *

```
>>> a = 5
>>> b = 6
>>> a + b
11
>>> a - b
-1
>>> a / b
0.8333333333333334
>>> a * b
30
>>> a % b
5
```

- Assignment Operators: =

```
>>> x = 10
```

- Relational Operators: <=, <, >, >=, ==, !=

```
>>> a = 5
>>> b = 6
>>> a < 6
True
>>> a > b
False
>>> a <= 5
True
>>> b >= 6
True
>>> a = 6
>>> a == b
True
>>> a != b
False
```

- Unary Operators: -

```
>>> u = 4
>>> -u
-4
>>> u = -u
>>> u
-4
```

- Logical Operators: and, or, not

```
>>> a == b and u > -2
False
>>> a == b and u < -2
True
>>> a == b or u > -2
True
>>> a != b or u < -2
True
>>> a = True
>>> not a
False
```

# Number System Conversion

- Decimal Number System: 0 to 9
- Binary Number System: 0 to 1
- Octal Number System: 0 to 7
- Hexadecimal Number System: 0 to 9, a to f

```
>>> bin(12)
'0b1100'
>>> 0b1100
12
>>> oct(12)
'0o14'
>>> 0o14
12
>>> hex(12)
'0xc'
>>> 0xe
14
```

# Swap 2 variables

- One method is to use a temporary variable to swap the values

```
>>> a = 3
>>> b = 4
>>> temp = a
>>> a = b
>>> b = temp
>>> a
4
>>> b
3
```

- Second method is to use arithmetic operation (addition)

```
>>> x = 4
>>> y = 5
>>> x = x + y
>>> y = x - y
>>> x = x - y
>>> x
5
>>> y
4
```

- Third method is to use XOR operator

```
>>> a = 5
>>> b = 6
>>> a = a ^ b
>>> b = a ^ b
>>> a = a ^ b
>>> a
6
>>> b
5
>>> 
```
