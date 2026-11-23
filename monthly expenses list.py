n = int(input("enter number of elements  "))

l1 = []

for i in range (n):

    l = int(input("enter number "))

    l1.append(l)

total = sum(l1)

print ("total annual expenditure ",total)

average = total / 12

print ("monthly average expense  ",average)

highest_expen = max(l1)

position = l1.index(highest_expen)

print = ("highest expenditure ",highest_expen)

print = ("months with highest expenditure  ",position + 1)

count = 0

for i in l1:

    if (i < 20000):

        count = count + 1

print ("monthly expenditure exceeded more than 20000  ",count)


