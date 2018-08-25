#programe to find the maximum three number from the list if first number from the list is not larger element. 

list=[66,75,4,45,77,234,45,-33,55,400,5000]
maximum=list[0]
llist=[]
for i in list:
        if i>maximum:
                maximum=i
		llist.append(maximum)
print(maximum)
print (llist[-3:])

