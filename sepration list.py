
l1 = []
l2 = []

print("Enter 20 numbers")

for i in range(20):
    n = int(input("Enter number: "))
    l1.append(n)

for i in l1:
    c = 0
    if i > 1:
        for j in range(1, i+1):
            if i % j == 0:
                c = c + 1

        if c == 2:
            l2.append(i)

print("Original list:", l1)
print("Prime numbers:", l2)
