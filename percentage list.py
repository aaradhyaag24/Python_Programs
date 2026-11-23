n = int (input("enter no. of elements "))

l = [0] * n

sum = 0

for i in range (n):

    l[i]= int(input("neter number "))

    sum = sum + (l[i])

    percentage  = sum / (n*100) * 100

print (l)

print ("sum",sum)

print ("percentage",percentage )