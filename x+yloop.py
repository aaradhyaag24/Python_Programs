n=int(input("enter n:"))
for i in range (1,n):
    if (i==1):
        if(i!=n):
            print("x+y/2",end = " , ")
        else:
            print("x+y/2",end = " ")
    else:
        if(i!=n):
            print("x^",i,"+y^",i,"/",2**i,end= " , ")
        else:
             print("x^",i,"+y^",i,"/",2**i,end= " ")