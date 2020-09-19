''' waopp for class circle to get radius and calculate the area, circumference'''


class circle:
	def __init__(self, r):
		self.radius = r
	def show(self):
		print("Radius= ", self.radius)
	def area(self):
		ans = 3.14159 * self.radius ** 2
		print("Area = ", round(ans,3))
	def circum(self):
		ans = 2 * 3.14159 * self.radius
		print("Circumference= ", round(ans,3))

rad = float(input("Enter radius: "))
c1 = circle(rad)
c1.show()
c1.area()
c1.circum()