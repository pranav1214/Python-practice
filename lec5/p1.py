''' function to find the sum of the digits'''

def sod(num):
	sum = 0 
	while num > 0:
		digit = num % 10
		sum = sum + digit
		num = num // 10 
	else:
		return sum

num = int(input("Enter the number: "))

if num < 0:
	print("Be positive")
else:
	ans = sod(num)
	print("Ans: ", ans)