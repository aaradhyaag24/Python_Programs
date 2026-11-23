n = int(input("Enter n: "))
fact = 1
for i in range(n, 0, -1):
    fact = fact * i
    if i == 1:
        print(i, end="=")
    else:
        print(i, end="*")
print(fact)