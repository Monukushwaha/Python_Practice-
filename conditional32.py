#check whether an alphabet is a vowel or consonant
vowel=["a","e","i","o","u"]
alpha=raw_input("enter alphabate : ")
if alpha not in vowel:
	print alpha + " is consonant. "
else:
	print alpha + " is vowel."
