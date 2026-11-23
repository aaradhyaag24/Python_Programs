n = int (input("enter number of elements"))

sum = 0

l = [0] * n

for i in range (n):

    l[i] = int(input("enter numbers  "))

    sum = sum + l[i]

print (l)

print ("sum",sum)