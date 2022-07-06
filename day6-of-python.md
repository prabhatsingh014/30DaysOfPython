# More on Variables

- id function can be used to identify the address of a variable where the value of the variable is stored in the memory
- assigning same value to multiple variable doesn't mean that all variables would have different address, all variables would refer to the address
- it's not the variable that is assigned the address, it's the value that is assigned the address
- if a value is not assigned to any variable, it becomes part of garbage collection

```
>>> a = 10
>>> b = a
>>> id(a)
4544922128
>>> id(b)
4544922128
>>> id(10)
4544922128
>>> 
>>> a = 9
>>> id(a)
4544922096
>>> id(b)
4544922128
>>> 
>>> c = a
>>> id(c)
4544922096
>>> id(9)
4544922096
>>> 
>>> 
>>> b = 8
>>> id(b)
4544922064
>>> 
>>> id(10)
4544922128
>>> 
```

- there is no concept of constants in the python programming language, but we can show our intent to declare some variable as a const such as PI = 3.14
- type() fuction is used to identify the data type of the variable

```
>>> PI = 3.14
>>> type(PI)
<class 'float'>
>>> 
>>> type(a)
<class 'int'>
>>> 
>>> name='prabhat'
>>> type(name)
<class 'str'>
>>>
```

# Data Types

- None: A variable which is not assigned any value like null in other programming languages
- Numeric: int, float, complex, bool
- Sequence: list, tuple, set, range, string
- Dictionary: key-value pair
- Complex type is represented in form of a+bj where j is the iota (as in mathematics)
- bool type is represented in the form of either True or False
- You can fetch the numeric value of bool values by using int fuction with bool
- range is represented in the form of (0,10) meaning 0,1,2,3,4,5,6,7,8,9
- there is no concept of constant as such in the python programming language, only string type is used for the constant as well as any string
- you can also display range in the form of the list using list function with range
- dictionary is represented in the form of key:value pair, since each key must be unique in a dictionary, it is enclosed in the curly braces like set

```
>>> a = 10
>>> type(a)
<class 'int'>
>>> b = 5.6
>>> type(b)
<class 'float'>
>>> 
>>> c = int(b)
>>> c
5
>>> 
>>> d = float(c)
>>> d
5.0
>>> f = 5+6j
>>> type(f)
<class 'complex'>
>>> 
>>> g=complex(a,b)
>>> g
(10+5.6j)
>>> 
>>> a < b
False
>>> b < a
True
>>> int(True)
1
>>> int(False)
0
>>> h = a<b
>>> h
False
>>> type(h)
<class 'bool'>
>>> 
>>> lst = [12,3,4,5,2,3,4,5]
>>> type(lst)
<class 'list'>
>>> 
>>> tuple = (2,3,4,5)
>>> type(tuple)
<class 'tuple'>
>>> 
>>> set = {1,2,3,4,5,6}
>>> type(set)
<class 'set'>
>>> 
>>> range(0,10)
range(0, 10)
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> a = range(10)
>>> a
range(0, 10)
>>> 
>>> 
>>> str1 = 'prabhat'
>>> type(str1)
<class 'str'>
>>> 
>>> str2 = 'a'
>>> type(str2)
<class 'str'>
>>> 
>>> 
>>> dict = {'name':'prabhat','age':35}
>>> dict
{'name': 'prabhat', 'age': 35}
>>> dict.key()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> dict.key
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> dict.keys()
dict_keys(['name', 'age'])
>>> 
>>> dict.values()
dict_values(['prabhat', 35])
>>> 
>>> dict.
dict.clear(      dict.fromkeys(   dict.items(      dict.pop(        dict.setdefault( dict.values(    
dict.copy(       dict.get(        dict.keys(       dict.popitem()   dict.update(    
>>> dict.
dict.clear(      dict.fromkeys(   dict.items(      dict.pop(        dict.setdefault( dict.values(    
dict.copy(       dict.get(        dict.keys(       dict.popitem()   dict.update(    
>>> dict.get('name')
'prabhat'
```
