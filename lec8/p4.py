#wapp to read rno and marks from user

class InvalidRnoException(Exception):
	def __init__(self, msg):
		self.msg = msg

class InvalidMarksException(Exception):
	def __init__(self, msg):
		self.msg = msg

try:
	rno = int(input("enter rno: "))
	if rno <= 0:
		raise InvalidRnoException("Rno cannot be -ve")
	marks = int(input("enter marks: "))
	if marks < 0 or marks > 100:
		raise InvalidMarksException("Marks out of range")
except ValueError:
	print("enter integers only")
except Exception as e:
	print("Issue: ", e)
else:
	print("Rno: ", rno, "Marks: ", marks)	