class rectangle:
	def __init__(self, le, br):
		self.length = le
		self.breadth = br
	def show(self):
		print("Length= ", self.length)
		print("Breadth= ", self.breadth)
	def area(self):
		ans = self.length * self.breadth
		print("Area= ", ans)
	def perimeter(self):
		ans = 2 * self.length + self.breadth
		print("Perimeter= ", ans)

le = float(input("Enter Length: "))
br = float(input("Enter Breadth: "))

r1 = rectangle(le, br)
r1.show()
r1.area()
r1.perimeter()
