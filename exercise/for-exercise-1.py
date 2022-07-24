# Write a program to print all the perfect squared number between 1 and 50

from math import sqrt


for num in range(1,51):
    s = num * num
    if s <= 50:
        print(s)