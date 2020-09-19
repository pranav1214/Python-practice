# to get a number and find its factorial

num = int(input("Enter a Number "))

if num < 0:
	print("Enter a valid number")

elif num == 0 and num == 1:
	print("Fact =", 1)

else:
	f=1
	for i in range (1, num+1):
		f *= i
	print("fact = ", f)