# to read a string and check if its a pallindrome

s1 = input("Enter a string: ")

r1 = s1[::-1]


if s1 == r1:
	print("Pallindrome")
else:
	print("Not a Pallindrome")
	