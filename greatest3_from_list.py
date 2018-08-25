list=[4,56,7,8,9,19,3,56]
list1=[]
for i in range(3):
	list1.append(max(list))
	list.remove(max(list))
print list1
