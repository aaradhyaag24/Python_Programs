n=int(input("enter n:"))
for i in range (1,n+1):
    if (i==n): 
        print ("x^",i+1,"+",1,"/",i*i+2,end = ",")
    else:
        print ("x^",i+1,"+",1,end=",")
