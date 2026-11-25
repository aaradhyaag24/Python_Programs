n=int(input("enter n "))
x =1
for i in range (n,0,-1):
    if (i>1):
        print (i, end = "*")
    else:
        print (i,end =" ")
    x= x*i
print("=",x)