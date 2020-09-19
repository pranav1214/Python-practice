class student:
	def __init__(self, r, n):
		self.rno = r
		self.name = n
	def talk(self):
		print("my rno is :", self.rno)
		print("my name is ", self.name)

s1 = student(10, "amit")
s2 = student(20, "sumit")
s3 = student(30, "rumit")


s1.talk()
s2.talk()
s3.talk()

# OOP : -> it is a way of solving a problem thru class and obj
#class: -> encapsulation -> var(rno, name) + method(__init__(), talk())
# reference -> s1, s2, s3
# self is not a keyword it is a preferred word and it contains object address	