#check password validity
password=raw_input(">>>>>>>")
u=0
l=0
d=0
s=0


for i in password:
    if i.isupper()==True:
        u+=1
    elif i.islower()==True:
        l+=1
    elif i.isdigit()==True:
        d+=1
    elif i=="@" or i=="#" or i=="$":
        s+=1
if len(password)>6 and len(password)<16:
    if u>0 and l>0 and d>0 and s>0:
        print"Valid Password"
    else:
        print"not valid"
else:
    print "not valid"
