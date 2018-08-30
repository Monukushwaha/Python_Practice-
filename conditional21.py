#programme for pattern of alphabate L:
for i in range(1,8):
    for j in range(1,8):
        if ((i<=6) and (j==2 or j==3 or j==4 or j==5)):
            print(" ",end="")
        elif (j<=5) and (i==1 or i>1 ) :
            print("*",end="")

            
    print()

