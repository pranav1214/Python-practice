# py prog for single inheritance person and student


class Person:
	def __init__(self, id, na ,ad):
		self.id = id
		self.name = na
		self.address = ad
	def show(self):
		print("id= ", self.id)
		print("name ", self.name)
		print("address= ", self.address)
class student(Person):
	def __init__(self, id, na, ad, ma):
		super().__init__(id, na, ma)
		self.marks = ma
	def show(self):
		super().show()
		print("marks = ", self.marks)
s = student(10, "amit", "Thane", 90)
s. show()
