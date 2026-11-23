n = int(input("Enter n: "))
i = 1
for j in range(n):
    print("x^", i, "+ y^", i, "/", 2**i)
    i = i + 1