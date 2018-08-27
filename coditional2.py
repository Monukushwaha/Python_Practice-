celsius=int(raw_input("enter the temprature in celsius"))
feh=int(raw_input("enter the temprature in fehrenhite "))

def conver(c,f):
	cel = (f-32)*5/9
	print str(feh)+'farenhite converted  to '+str(cel) + " degree celcius"
	F = c/5*9+32
	print str(celsius)+ " degree celsius have "+ str(F) + "  fehrenhite"
conver(celsius,feh)
