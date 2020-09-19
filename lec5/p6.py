# write a menu driven program to implement data structure
# queue/ fifo

queue = []
while True:
	op = int(input("1:insert, 2:pop, 3:Display, 4: Exit "))
	if op == 1:
		ele = int(input("Enter the element to insert: "))
		queue.append(ele)
		print(ele, " is inserted in the queue")
	elif op == 2:
		if len == 0:
			print("queue is empty")
		else:
			ele = queue.pop(0) 
			print(ele, "is popped")
	elif op == 3 :
		print(queue)
	elif op == 4:
		break
	else:
		print("invalid option")