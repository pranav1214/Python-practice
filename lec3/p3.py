# generate the following pattern
#	10
#	20	20
#	30	30	30
# n would be provided by user

num = int(input("Enter number of lines to generate: "))

if num < 0:
	print("Invalid number")

else:
	k = 10
	for j in range (1, num+1):
		print(j * (str(k)+ "\t"))
		k = k+ 10