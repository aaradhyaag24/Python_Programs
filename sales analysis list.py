
sales = []

for i in range(15):

    n = int(input("Enter sales: "))

    sales.append(n)

print("Highest Sales:", max(sales))

print("Lowest Sales:", min(sales))

total = sum(sales)

average = total / 15

print("Total Sales:", total)

print("Average Sales:", average)

count = 0

for i in sales:

    if i > average:

        count = count + 1

print("Days above average:", count)

l2 = sales.copy()

l2.sort(reverse=True)

print("Second Highest Sales:", l2[1])

l3 = sorted(sales, reverse=True)

print("Original List:", sales)

print("Descending Order:", l3)
