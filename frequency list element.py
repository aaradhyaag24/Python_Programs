n = int (input("enter number of elements "))

l1 = []

l2 = []

for i in range (n):

    l = int(input("enter number "))

    l1.append(l)

for i in l1 :

    if i not in l2:

        print (i, "occurs", l1. count(i), "times")

        l2.append(i)
