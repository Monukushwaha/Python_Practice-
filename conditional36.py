x=int(raw_input("enter the length of side 1st  of a traingle : "))
y=int(raw_input("enter the length of side 2nd of a traingle : "))
z=int(raw_input("enter the length of side 3rd of a traingle : "))
if x==y and y==z and z==x:
	print("traingle is equilateral triangle ")
elif ((x==y and y==z) or z==x) or ((x==y and z==x) or y==z) or ((y==z and  z==x) or x==y):
	print("traingle is isosceles traingle ")
else:
	print(" traingle is scalene triangle ")
