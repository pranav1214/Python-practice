# generate the following pattern
#	a
#	b	b
#	c	c	c
#	d	d	d	d
# n would be provided by user

num = int(input("Enter the number to generate lines: "))

if num < 0:
	print("Invalid number")

else:
	c = 97
	for i in range(1, num+1):
		print(i * (chr(c)+ "\t"))
		c = c + 1
