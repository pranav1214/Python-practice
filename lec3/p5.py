# generate the following pattern
#	*	*   *   *
#	*	*	*
#	*	*
#	*
# n would be provided by user

num = int(input("Enter the number to generate lines: "))

if num < 0:
	print("Invalid number")

else:
	for i in range(num,  0, -1):
		print(i * ("*" + "\t"))
		