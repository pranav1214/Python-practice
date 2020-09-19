# to read a number and find the reverse of the number

num = int(input("Enter a number"))

if num < 0:
	print("Invalid input")

else:
	print("num = ", num)
	rev = 0
	while num > 0:
		digit = num % 10
		rev = rev * 10 + digit
		num = num // 10
	else:
		print("rev = ", rev)

