n = int(input("enter number of elements  "))

l1 = []

l2 = []

for i in range (n):

    l = int(input("emter no.  "))

    l1.append(l)

for i in l1:

    if (i != 0):

        l2.append(i)

for i in l1:

    if (i == 0):

        l2.append(i)

print ("original list ",l1)

print ("updated list ",l2)

