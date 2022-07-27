# Write a program to print first 50 fibonacci numbers
# 0 1 1 2 3 5 8 13
i = 0
j = 1
count = 1
while count <= 50:
    sum = i + j
    print(sum)
    i = j
    j = sum
    count += 1