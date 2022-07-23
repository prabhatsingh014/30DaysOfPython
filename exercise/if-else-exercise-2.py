# Write a program to take three values from user and find the greatest number from them
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x > y and x > z:
    print("Greatest number is " + str(x))
elif y > x and y > z:
    print("Greater number is " + str(y))
elif z > x and z > y:
    print("Greatest number is " + str(z))