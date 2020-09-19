class mech:
	def __init__(self, price):
		self.price = price
	def __add__(self ,other):
		ans = self.price + other.amount
		return ans
	def __sub__(self ,other):
		ans = self.price - other.amount
		return ans

class bee:
	def __init__(self, amount):
		self.amount = amount
	def __sub__(self ,other):
		ans = self.amount - other.price
		return ans

m = mech(750)
b = bee(350)

r1 = m + b
print(r1)

r2 = m - b
print(r2)

r3 = b - m
print(r3)