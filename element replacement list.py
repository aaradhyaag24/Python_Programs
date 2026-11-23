n = int(input("emter no. of elements "))

l1 = []

l2 = []

for i in range (n):

    l = int(input("enter no. "))

    l1.append(l)

for i in l1:

    if (l1.count(i)>1):

        l2.append(-1)

    else:

        l2.append(i)

print ("original list ",l1)

print ("modified list ",l2)


