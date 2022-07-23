# Write a code to print all the values from 1 to 100.
# Skip the numbers which are divisible by 3 or 5.

from sre_constants import JUMP


num = 1
while num <= 100:
    if (num % 3) == 0 or (num % 5) == 0:
        pass
    else:
        print(num)
    num = num + 1