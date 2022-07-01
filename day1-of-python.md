## Python Introduction, Print Functions, Literals, Operators

```
>>> print ("Hello future Python programmer")
Hello future Python programmer
>>> print ("Hello future Python programmer!")
Hello future Python programmer!
>>> print ("Hello future", end="!")
Hello future!>>> 

>>> print ("Python programmer!, sep="-");\
... 
  File "<stdin>", line 1
    print ("Python programmer!, sep="-");\
                                      ^
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> print ("Python programmer!", sep="-")
Python programmer!
>>> print ("Python programmer!", sep="..")
Python programmer!
>>> 
>>> print ("Hello future python programmer", sep="-")
Hello future python programmer
>>> print ("Hello", "future", "python", "programmer", sep="-")
Hello-future-python-programmer
>>> 
>>> print("Hello \"Python\" world")
Hello "Python" world
>>> print('My age is ' + 25)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print(1, 2, 3, 4, sep='#', end='&')
1#2#3#4&>>> 
>>> 
>>> print("Hello" + " " "future" + " " "python!")
Hello future python!
>>> print(10-6**7/9*10+1)
-311029.0
>>> print(10-6**2/9*10+1)
-29.0
>>> print(2*(2+3))
10
>>> print(10-6**2/9*10+1)
-29.0
>>> print(10-6**2//9*10+1)
-29
>>> print(6. // 4)
1.0
>>> print(2 ** 3.)
8.0
>>> print(2 * 3 ** 3 * 4)
216
>>> print(13 / 4 + 13 % 4)
4.25
>>> print(100 / 50)
2.0
>>> print(10 / 2)
5.0
>>> print(2 ** 3)
8
>>> x = 10 / 4
>>> y = 5 / 2.0
>>> print(x + y)
5.0
>>> print(20 / 5 * 4)
16.0
>>> 
```
