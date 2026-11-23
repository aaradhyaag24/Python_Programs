n = int(input("enter number of elements "))

l1 = []

l2 = []

print ("list 1  ")

for i in range (n):

    l = int(input("enter number "))

    l1.append(l)

print ("list 2  ")

for i in range (n):

    y = int(input("enter number "))

    l2.append(y)

l3 = l1 + l2 

print ("merged list ",l3)

