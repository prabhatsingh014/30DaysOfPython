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
    print("*", end=" ")
    while j < 5:
        print('#', end=" ") # print on the same line instead of new line
        j = j + 1 # decrease value of j by 1
    i = i + 1 # decrease value of i by 1
    print() # print on new line