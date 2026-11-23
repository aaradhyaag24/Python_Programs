n=int(input("enter value:"))
x=1
for i in range (1,n+1):
    if (i%2!=0):
        if(i==1):
            x=i*2
            print(x,"x")
            x=i*4
            print(x,"x")
        else:
            x=i*2
            print(x,"x")
    else:
        x=i*4
        print(x,"x")
    

