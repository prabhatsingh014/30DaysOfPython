# Lists

- list is a type of variable which can consists of multiple values, be it integer, string or floating point number
- list can have single as well as multiple type of values e.g. a list can have value which are either all integers or it can also have a combination of integers as well as strings as well as floating point numbers whereas array can have only one type of values
- you can also pick up the values based on the index number which starts with 0 from the start or -1 from the en

```
>>> num = [1,4,6,8,9]
>>> print(num[0])
1
>>> print(num[4])
9
>>> print(num[9])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> 
>>> print(num[-1])
9
>>> print(num[-5])
1
>>> 
>>> # you can also print range of value using colon
>>> 
>>> print(num[0:2])
[1, 4]
>>> print(num[1:3])
[4, 6]
>>> print(num[2:])
[6, 8, 9]
>>> print(num[:4])
[1, 4, 6, 8]
>>> print(num[-1:])
[9]
>>> 
>>> names = ['prabhat', 'singh', 'india', 'uttar', 'pradesh']
>>> print(names[0])
prabhat
>>> 
>>> 
>>> 
>>> names = [13, 'prabhat', 9.5]
>>> print(names[])
  File "<stdin>", line 1
    print(names[])
          ^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> print(names)
[13, 'prabhat', 9.5]
>>> 
>>> 
>>> print(names[1])
prabhat
>>> 
>>> 
>>> # you can also have list of lists
>>> 
>>> combinelist = [num, names]
>>> print(combinelist)
[[1, 4, 6, 8, 9], [13, 'prabhat', 9.5]]
>>> 
>>> print(combinelist[0])
[1, 4, 6, 8, 9]
>>> 
>>> 
>>> print(combinelist[1])
[13, 'prabhat', 9.5]
>>> print(combinelist.num[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'num'
>>> 
>>> print(combinelist[].num[3])
  File "<stdin>", line 1
    print(combinelist[].num[3])
          ^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
```
 
- lists are mutable which means  you can add values to list

```
>>> num.append(5)
>>> print(num)
[1, 4, 6, 8, 9, 5]
>>> 
>>> num.
num.append(   num.copy()    num.extend(   num.insert(   num.remove(   num.sort(    
num.clear()   num.count(    num.index(    num.pop(      num.reverse()
>>> num.
num.append(   num.copy()    num.extend(   num.insert(   num.remove(   num.sort(    
num.clear()   num.count(    num.index(    num.pop(      num.reverse()
>>> num.append(3)
>>> print(num)
[1, 4, 6, 8, 9, 5, 3]
>>> 
>>> 
```
