# to read a string and count the number of letters, #digits and other

s1 = input("Enter a string: ")

lc, dc, oc = 0, 0, 0 

for s in s1:
	if (('A' <= s <= 'Z') or ('a' <= s <= 'z')):
		lc = lc + 1
	elif ('0' <= s <= '9'):
		dc = dc + 1
	else:
		oc = oc + 1

print("Letters: ", lc, "Digits: ", dc, "Other: ", oc)

