class person:
	def __init__(self, id, na, ad):
		self.id = id
		self.name = na
		self.address = ad
	def show(self):
		print("id= ", self.id)
		print("name= ", self.name)
		print("address= ", self.address)
class student(person):
	def __init__(self, id, na, ad, ma):
		super().__init__(id, na, ad)
		self.marks = ma
	def show(self):
		super().show()
		print("marks=", self.marks)
class sport:
	def __init__(self, me):
		self.medals = me
	def show(self):
		print("medals= ", self.medals)

class result(student, sport):
	def __init__(self, id, na, ad, ma, me):
		student.__init__(self, id, na, ad, ma)
		sport.__init__(self,me)

r = result(10, "amit", "thane", 98 ,2)
r.show()	