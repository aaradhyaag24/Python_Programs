n = int(input("enter number of elements "))

l1 = []

l2 = []

l3 = []

print ("elements for list 1")

for i in range (n):

    j = int(input("enter number"))

    l1.append(j)

print ("elements for list 2")

for i in range (n):

    k = int(input("enter number "))

    l2.append(k)

print("common elements of list 3")

for i in l1:

    for j in l2:

        if (i == j) and (i not in l3):

            print (i)

            l3.append(i)





