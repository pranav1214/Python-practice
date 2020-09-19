






class employee:
	ceo_name = "ABC"
	def __init__(self, id, na, sa):
		self.eid = id
		self.ename = na
		self.esalary = sa
	def display(self):
		print("id = ", self.eid)
		print("name = ", self.ename)
		print("salary = ", self.esalary)
	def compute_taxes(self):
		if self.esalary < 0:
			print("Enter valid salary")
		elif self.esalary > 5000:
			ans = self.esalary * 0.2
			print("taxes to be paid= ", ans)
		else:
			ans = self.esalary * 0.1
			print("taxes to be paid= ", ans)
	@staticmethod
	def display_ceo():
		print("ceo name = ", employee.ceo_name)	

e1 = employee(20, "amit", 6000)
e1.display()
e1.compute_taxes()
e1.display_ceo()
employee.display_ceo()