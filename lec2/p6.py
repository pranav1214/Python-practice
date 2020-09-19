# to find sum of n +ve integers
# i/p =5        1+2+3+4+5 =15

num = int(input("Enter a positive integer: "))

if num < 0:
	print("Invalid Input")

else:
	sum,i = 0,1
	while i <= num:
		sum = sum + i
		i = i + 1
	print("Sum= ", sum)