n=int(input("enter n:"))
x=int(input("enter n:"))
total=0
for i in range(n, 0, -1):
    print(i,"x","+",end= " ")
    total= total+(i*x)
    print(total,end= "+")
    if (i!=1):
        print("+",end=" ")
