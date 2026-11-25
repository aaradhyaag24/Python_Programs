x = int(input("enter number of elements  "))

l1 = []

l2 = []

print("Enter numbers")

for i in range(x):

    n = int(input("Enter number: "))

    l1.append(n)

for i in l1:

    count = 0

    if i > 1:

        for j in range(1, i+1):

            if i % j == 0:

                count = count + 1

        if count == 2:

            l2.append(i)

print("Original list:", l1)

print("Prime numbers:", l2)
