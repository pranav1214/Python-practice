# find factorial using function


def fact(num):
	if num == 1:
		return 1
	else:
		return num * fact(num -1)

num = int(input("Enter a number: "))

if num < 0:
	print("Enter a positive number")
elif num == 0 or num == 1:
	print("fact= ",1)
else:
	ans = fact(num)
	print("fact= ",ans)