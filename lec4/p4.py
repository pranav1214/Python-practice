'''
accept a string of numbers and add them
'''

s1 = input("Enter a string: ")

d1 = s1.split(",")

sum = 0 

for d in d1:
	sum = sum + int(d)

print(sum)