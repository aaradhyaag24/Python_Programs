n=int(input("enter n "))
for i in range (1,n+1):
    print("1/", end = " ")
    for j in range (1,i+1):
        if (j!=i):
            print (j,end = "+")
        else:
            print (j,end = " ")
    if (i!=n):
        print (end = ",")
    else:
        print (end = " ")