#wapp to read marks and find grade
# m >= 70 = distinction, m>=60 = first class
# m >=50 = second class , m >= 40 = fail

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
	print("Marks not in Range")
elif marks >= 70:
	print("Distinction")
elif marks >= 60:
	print("First Class")
elif marks >= 50:
	print("Second Class")
elif marks >= 40:
	print("Pass Class")
else:
	print("Fail")