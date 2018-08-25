list=["monu","shivam","harshit","amar","umesh"]
empty_list=[]
for name in list:
	for j in range(len(name)):
		if "m" and "o" in name[j]:
			empty_list.append(name)
print(empty_list)
				
	
