# to generate the following pattern
# A	A	A	A
# B	B	B
# C	C
# D

num = int(input("Enter number to generate pattern: "))

if num < 0:
	print("be  +ve")

else:
	c = 65 
	for i in range(num,  0, -1):
		print(i * (chr(c) + "\t"))
		c = c + 1