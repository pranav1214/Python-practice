# read 3 int and find the max

n1 = int(input("Enter First number"))
n2 = int(input("Enter Second number"))
n3 = int(input("Enter Third number"))

if n1 > n2:
	m1=n1
else:
	m1=n2

if n3 > m1:
	m1=n3

print("Max of 3= ", m1)

res = max(n1, n2, n3)
print("Result= ", res)
