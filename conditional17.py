# program to print alphabet pattern 'A'.
for i in range(1,7):
        for j in range(0,5):
            if (j==0 and i==1) or (j==0 and i==5) :
                print (" ",end="")
            elif (j==0 ) and (i<5):
                print("*",end="")

print()
for i in range(1,7):
        for j in range(0,7):
            if (j==0 or j==4) and (i!=0 ) or (i==3 and j<5):
                print("*",end="")
            elif (j!=0 or j!=4):
                print (" ",end="")
        print("")
