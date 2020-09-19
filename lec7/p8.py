class book:
	def __init__(self, nop):
		self.nop = nop
	def __add__(self, other):
		res = self.nop + other.nop
		return res
	def __sub__(self, other):
		res = self.nop - other.nop
		return res
	def __mul__(self, other):
		res = self.nop * other.nop
		return res

b1 = book(100)
b2 = book(200)

r1 = b1 + b2
print(r1)
r2 = b1 - b2
print(r2)
r3 = b1 * b2
print(r3)

	