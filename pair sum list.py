n = int(input("enter number of elements "))

target_num = int(input("emter target number  "))

l1 = []

for i in range (n):

    l = int(input("enter number "))

    l1.append(l)

print ("pairs are ")

for i in range (n):

    for j in range (i +1,n):

        if (l1[i] + l1[j] == target_num):

            print (l1[i], l1[j])



