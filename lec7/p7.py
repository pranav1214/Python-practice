class employee:
	def __init__(self, id, na, sa):
		self.id = id
		self.name = na
		self.salary = sa
	def bonus(self):
		amt = self.salary * 0.10
		print("bonus amt= ", amt)

class aemployee(employee):
	pass

class pemployee(employee):
	def bonus(self):
		amt = self.salary *0.15
		print("bonus amt= ", amt)

class manager(employee):
	def bonus(self):
		amt = self.salary * 0.20
		print("bonus amt= ", amt)

a = aemployee(10, "amit", 1000)
a.bonus()
p= pemployee(20, "sumit", 2000)
p.bonus()
m = manager(30, "rumit", 5000)
m.bonus()