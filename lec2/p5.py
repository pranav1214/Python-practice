# to read attendance 

attdn = int(input("Enter attendance: "))

if attdn <=0:
	print("Invalid Input")

else:
	i=1
	while i<= attdn:
		print("Present", i)
		i = i+1
	print("attendance complete")