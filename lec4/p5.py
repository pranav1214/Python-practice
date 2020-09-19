'''accept a csv and print it
i/p: a,2,b,4,c,3
o/p :  a  a
       b  b  b  b
       c  c  c 
'''

s1 = input("Enter a string: ")

d1 = s1.split(",")

for i in range(0, len(d1),2):
	what = d1[i] + "\t"
	how = int(d1[i+1])
	print(what * how)