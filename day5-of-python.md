# Tuple

- tuple is like list which can contain multiple values, but it is immutable element of python meaning the value, once defined, cannot be changed
- tuple consists of values in the circular brackets unlike list which contains values in square brackets
- with list, we have multiple methods that can be used to manipulate the values within a list, however, with tuple, only 2 methods are present, one is count and other is index
- tuple is used when you don't want to change the values within it, due to which, it's faster to process
```
>>> tup = (10,20,30,40,50)
>>> print(tup)
(10, 20, 30, 40, 50)
>>> print(tup[0])
10
>>> print(tup[-1])
50
>>> print(tup[2:3])
(30,)
>>> print(tup[0:3])
(10, 20, 30)
>>> 
>>> print(tup[:3])
(10, 20, 30)
>>> print(tup[2:])
(30, 40, 50)
>>>
```
- if you try to change the value in a tuple

```
>>> tup[1] = 33
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

# Set

- set is like list or tuple but it differs from list or tuple in the way that it doesn't support indexing
- you can't add or remove or update the value in a set
- with set, you cannot accpet any sequencing in the elements
- set only contains the unique values meaning if you define the duplicate values in a set, it will automatically be removed
- with set, values are enclosed in the curly braces

```
>>> s = {10,3,4,5,6,7,2,34}
>>> s
{2, 3, 4, 5, 6, 7, 34, 10}
>>> 
>>> s = {43,13,456,132,134,245,13}
>>> s
{132, 245, 134, 456, 43, 13}
>>> 
>>> # notice the duplicate value has been removed
>>> 
>>> # if you try to update any value in the set
>>> s[0]=321
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support item assignment
>>> 
```
