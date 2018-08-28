a=int(raw_input("enter the number1 : ")) 
b=int(raw_input("enter the number2 : "))
c=int(raw_input("enter the number3 : "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median is  "+ str(median))

