n=int(input("enter n"))
for i in range (2,n+2):
    if (i<=n):
        print(i,"/",i*i,end = ",")
    else:
        print(i,"/",i*i,end = " ")

