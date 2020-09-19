# to read list of marks from user and print
# sum of marks, average, minimum and maximum


marks = []
res = input("do you want to add some marks y/n: ")
while res == 'y':
	m = int(input("pls provide marks: "))
	marks.append(m)
	res = input("do want to add more marks y/n: ")

sum = 0
for m in marks:
	sum = sum + m
print("Sum= ", sum)

avg = sum / len(marks) ; print("Avg= ", avg)
m1 = min(marks) ; print("Minimum= ", m1)
m2 = max(marks) ; print("Maximum= ", m2)


marks.sort()
m3 = marks[0] ; print("Min= ", m3)
m4 = marks[-1] ; print("Max= ", m4)