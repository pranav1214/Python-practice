#wapp to read rno and marks from user

try:
	rno = int(input("Enter rno "))
	if rno < 0:
		raise Exception("rno cannot be -ve ")
	marks = int(input("Enter marks"))
	if marks < 0 or marks > 100:
		raise Exception("marks out of range")
except ValueError:
	print("enter integers only")
except Exception as e:
	print("Issue: ", e)
else:
	print("Rno: ", rno, "Marks: ", marks)