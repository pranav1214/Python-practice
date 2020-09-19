# write a menu driven program to implement data structure
# stack/ lifo/ filo

stack = []
while True:
	op = int(input("1:push. 2:pop, 3:Display, 4: Exit"))
	if op == 1:
		ele = int(input("Enter the element: "))
		stack.append(ele)
		print(ele, " is pushed in the stack")
	elif op == 2:
		if len == 0:
			print("Stack is empty")
		else:
			ele = stack.pop() 
			print(ele, "is popped")
	elif op == 3 :
		print(stack)
	elif op == 4:
		break
	else:
		print("invalid option")