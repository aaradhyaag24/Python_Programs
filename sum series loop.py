n=int(input("enter n"))
sum=0
for i in range (1,n+1):
    if (i==1):
        print (i,"/",i+1,end = "+")
        sum = sum + i /(i +1)
    else:
        print(i,"/",i+1,end = "+")
        sum = sum + i / (i + 1)
print ("sum",sum)
        