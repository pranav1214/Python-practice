#to read a str and count number of letter, digits and #other characters


s1 = input("Enter a string: ")

lc,dc,oc = 0,0,0

for s in s1:
	if s.isalpha():
		lc = lc+1
	elif s.isdigit():
		dc = dc+1
	else:
		oc= oc+1
print("letters= ",lc, "digits= ",dc, "Others= ",oc)