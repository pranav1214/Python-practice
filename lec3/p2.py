# generate the following pattern
#	*
#	*	*
#	*	*	*
# n would be provided by user

num = int(input("Enter number of lines to generate: "))

if num < 0:
	print("Invalid number")

else:
	for i in range (1, num+1):
		print(i * "*\t")