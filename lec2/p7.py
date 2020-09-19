# read a number and find the sum of digits
# i/p : 132 op : 1+3+2

num = int(input("Enter a number"))

if num < 0:
	print("Invalid input")
else:
	sum = 0 
	while num > 0:
		digit = num % 10
		sum = sum + digit
		num = num // 10

	print("Sum = ", sum) 