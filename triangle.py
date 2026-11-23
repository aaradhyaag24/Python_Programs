a=int(input("enter value"))
b=int(input("enter value"))
c=int(input("enter value"))
if ((a+b>c) and (a+c>b) and (b+c>a)):
    print("valid triangle")
    x=1
else:
    print("invalid triangle")
    x=0
    if (x==1):
        if ((a==b)and (b==c)and (c==a)):
            print("equilateral")
        elif ((a==b)and (b==a)and (a!=c)):
                                       print("isocelence")
        elif((a!=b)and(b!=c)and (c!=a)):
                print("scalence")
        else:
                print("invalid")

