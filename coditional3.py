import random
import sys
i=1
guess=0
num=random.randint(1,9)
while i<=9:
	guess=int(raw_input("enter number"))
	if guess==num:
		print"well guessed"
		sys.exit()
	else:
		print"again until the guess is correct"
	i=i+1
