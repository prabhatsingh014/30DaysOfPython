# Write a program to print the following output
# *
# * *
# * * *
# * * * *
# * * * * *

i = 1 #initialize i
#j = 5
while i <= 5:
    j = 1 # initialize j. value of j would decrease with the value of i
    while j <= i:
        print('#', end=" ") # print on the same line instead of new line
        j = j + 1 # increase value of j by 1
    i = i + 1 # increase value of i by 1
    print() # print on new line