n = int(input("Enter n: "))

for i in range(1, n+1):
    if i % 2 != 0:
        x = 500 - ((i+1)//2)*100
    else:
        x = 500 - (i//2)*100

    if i == n:
        print(x, end="")
    else:
        print(x, end=",")
