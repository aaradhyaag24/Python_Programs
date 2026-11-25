n=int(input("enter n "))
sum = 1
for i in range (1,n+1):
    sum = sum *i
    if (i==n):
        print (i,end = "*")   
    else:
        print (i,end = "*")
print ("=",sum)

