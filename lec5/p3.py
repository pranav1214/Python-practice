# to read list of marks from user and print

marks = []

res = input("do you want to add some marks y/n: ")
while res == 'y':
	m = int(input("pls provide marks: "))
	marks.append(m)
	res = input("Do you want to add more marks y/n: ")

print(marks)

for m in marks:
	print(m)

for m in marks:
	print(m, end = ' ')