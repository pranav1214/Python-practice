class person:
	def __init__(self, id, na, ad):
		self.id = id
		self.name = na
		self.address = ad
	def show(self):
		print("id= ", self.id)
		print("name= ", self.name)
		print("address= ", self.address)
class teacher(person):
	def __init__(self, id, na, ad, sa):
		super().__init__(id, na, ad)
		self.salary = sa
	def show(self):
		super().show()
		print("salary = ", self.salary)
class hod(teacher):
	def __init__(self, id ,na, ad, sa, de):
		super().__init__(id, na, ad, sa)
		self.dept = de
	def show(self):
		super().show()
		print("Dept= ", self.dept)
h= hod(10, "amit", "thane", 7000, 'comps')
h.show()

t = teacher(12, "pol", "chunabhatti",5000)
t.show()