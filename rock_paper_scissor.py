user1=raw_input("enter the input rock or scissor or paper>>>>>>")
user2=raw_input("enter the input2 rock or scissor or paper>>>>>")

def game(u1,u2):
	if u1==u2:
		return("game tie ")
	elif u1=="rock":
		if u2=="scissor":
			return("rock wins ")
		else:
			return("paper wins")
	elif u1=="scissor":
		if u2=="paper":
			return("scissor wins")
		else:
			return("rock wins")
	elif u1=="paper":
		if u2=="rock":
			return("paper wins")
		else: 
			return("scissor wins")
	else:
		return("enter right input ")


print (game(user1,user2))
