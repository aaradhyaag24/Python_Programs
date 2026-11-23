n = int (input("enter number of elements  "))

sum = 0

l = [0] * n

for i in range(n):

    l[i] = int(input("enter number  "))

    sum = sum + (l[i])

    average = sum / n

print (l)

print("sum",sum)

print ("average",average)