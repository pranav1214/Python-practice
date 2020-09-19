''' function to find the sum of the digits - recursively'''

def sod(num):
	if num == 0:
		return 0
	else:
		return (num % 10) + sod(num // 10)

num = int(input("Enter the number: "))

if num < 0:
	print("Be positive")
else:
	ans = sod(num)
	print("Ans: ", ans)