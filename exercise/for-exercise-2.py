# Write a program to print the following pattern
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5):
    for j in range(5-i):
        print('* ', end="")
    i += 1
    print()