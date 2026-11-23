n=int(input("enter n "))
for i in range (2,n+1):
    if (i==2):
        print("x^",i,"+",(i+1),"/",i+(i+1),end = ",")
    else:
        print("x^",i,"+",(i+1),"/",i+(i+1),end = " ")

