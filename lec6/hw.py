# to maintain station names with corona count

corona_counter = { }
while True:
    op = int(input("1 add, 2 view, 3 update, 4 remove, 5 exit"))
    if op == 1:
        sn = input("Enter Station Name: ")
        ch = corona_counter.get(sn)
        print(ch, corona_counter)
        if ch == None:
            co = int(input("Enter Count: "))
            corona_counter[sn] = co
            print(sn, " has been added ")
        else:
            print(sn," already exists ")
            print(ch)
    elif op == 2:
        print(corona_counter)
    elif op == 3:
        sn = input("Enter Station name to be updated: ")
        co = int(input("Enter Count: "))
        corona_counter[sn] = co
        corona_counter.update[sn]
    elif op == 4:
    
    
    elif op == 5:
        break
    else:
        print(" ")