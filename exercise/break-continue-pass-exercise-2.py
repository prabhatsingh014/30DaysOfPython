# A school method based Python3
# program to check if a number
# is prime


def isPrime(n):

	# Corner case
	if n <= 1:
		return False

	# Check from 2 to n-1
	for i in range(2, n):
		if n % i == 0:
			return False

	return True


# Driver Program to test above function
num = int(input("Enter the number: "))
print("true") if isPrime(num) else print("false")

# This code is contributed by Smitha Dinesh Semwal
