#convert decimal to binary  using python programme
num=int(raw_input("enter number: "))
b=''
while num>=1:
        if num%2==0:
            b=b+"0"
        else:
                b=b+"1"
        num=num//2
print(b)
