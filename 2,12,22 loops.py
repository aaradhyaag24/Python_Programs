n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i == 1:
        print(2, end="")
    else:
        print(10 * (i - 1) + 2, end="")
    if i != n:
        print(",", end=" ")
