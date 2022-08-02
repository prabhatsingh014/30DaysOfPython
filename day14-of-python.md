# For else in Python
- Unlike any other programming languages, you can use else with a for loop
- Let's suppose you'd like to run a for loop within which a statement has to be run based on a condition using "if" and other statement if condition is not satisfied using "else". Example of one such sample is given below.
```
nums = [11,12,65,42,69]

for num in nums:
    if num % 5 == 0:
        print("Great")
    else:
        print("Not Great")
```
- The output of which comes out to be
```
Not Great
Not Great
Great
Not Great
Not Great
```
- In this example, if a number is not divisible by 5, else statement is printed as long as the for loop runs
- To avoid the execution of else statement multiple time and print the else statement when it finds the if condition to not be true, you can use "else" with "for" loop as
```
nums = [11,12,65,42,69]

for num in nums:
    if num % 5 == 0:
        print("Great")
        break
else:
    print("Not Great")
```
- Output of above program comes out to be ``Great``.
- Notice the usage of break within "if" block
- Another scenarios is the one in which no condition matched within "if" block, in that case, Not Greate is printed only once
```
nums = [11,12,66,42,69]

for num in nums:
    if num % 5 == 0:
        print("Great")
else:
    print("Not Great")
```
- Output of above program comes out to be ``Not Great``.