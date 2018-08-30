# Python program to print alphabet pattern 'G':
for i in range(1,8):
    for j in range(1,8):
        if ((i==1 or i==7 ) and (j==1 or j==5)) or ((j==2 or j==3 or j==4 ) and (i==2 or i==3 or i==5 or i==6) or ( i==3 and j==5) or (i==4 and j==2)):
            print(" ",end="")
        elif (i<8 and j<6):
            print("*",end="")
    print()


