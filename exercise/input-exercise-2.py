# Write a program to find out the cube of a given number input provided from the command line

import sys as s
num = int(s.argv[1])
res = num * num * num
print(res)