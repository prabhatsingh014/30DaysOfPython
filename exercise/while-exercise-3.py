# Write a program to print the following output
# * * * * *
# * * * *
# * * *
# * *
# *

i = 5 #initialize i
#j = 5
while i >= 1:
    j = i # initialize j. value of j would decrease with the value of i
    while j >= 1:
        print('*', end=" ") # print on the same line instead of new line
        j = j - 1 # decrease value of j by 1
    i = i - 1 # decrease value of i by 1
    print() # print on new line