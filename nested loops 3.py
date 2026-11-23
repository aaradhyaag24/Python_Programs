n = int (input("enter n"))
for i in range (1,n+1):
    for j in range (1,2):
        print (7*i,"/",6*i,end = " ")
        print ("*1",end = "")
    if (i!=n):
        print (end = ",")
    else:
        print (end = " ")
