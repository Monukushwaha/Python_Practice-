calc=raw_input(" enter the string ")
letter=0
digit=0
for str in calc:
	if str.isdigit()==True:
		digit+=1
	elif str.isalpha()==True:
		letter+=1
print(digit)
print(letter)
