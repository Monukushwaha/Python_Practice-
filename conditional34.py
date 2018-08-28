# if sum of two number is between 15 to 20 its should return 20.
num1=int(input())
num2=int(input())

def add(a,b):
        s=a+b
        if s>15 and s<20:
                return(20)
	else:
		return s
add(num1,num2)
