# to find factorial using function

def fact(num):
	f =1 
	for i in range(1,num+1):
		f = f*i
	else:
		return f

num = int(input("Enter a number: "))
	
if num < 0:
	print("Enter a positive number")
elif num == 0 or num == 1:
	print("Fact= ", 1)
else:
	ans = fact(num)
	print("fact= ",ans)