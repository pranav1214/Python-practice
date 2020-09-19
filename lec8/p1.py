# read two int and find n1/n2

print("Processing Started")

try:
	n1 = int(input("Enter first number: "))
	n2 = int(input("Enter second number: "))
	res = n1/n2
except ValueError:
	print("You need to enter integers only")
except ZeroDivisionError:
	print("second number should not be 0")
else:
	print("Res= ", res)
print("Processing Ended")