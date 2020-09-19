# read an int and find if its evn or odd

num = int(input("Enter the number: "))

res = num % 2
if res == 0:
	print("Number is even")
else:
	print("Number is odd")

if num % 2 == 0 :
	print("Even")
else:
	print("Odd		")