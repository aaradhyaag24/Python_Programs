n = int(input("enter n: "))
p = 2
d = 4
for i in range(2, n + 1):
    if i == 2:
        print("x^2+y^2/4*1", end="")
    else:
        print("x^" + str(p) + "+y^" + str(p) + "+z^" + str(p) + "/" + str(d) + "*1", end="")
    if i < n:
        print(", ", end="")
    if i == 2:
        p = 8
    else:
        p = p * 2
    d = d * 2