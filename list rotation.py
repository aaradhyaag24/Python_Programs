L = [10, 20, 30, 40, 50]

n = int(input("Enter number of rotations: "))

for i in range(n):
    x = L.pop(0)
    L.append(x)

print("Rotated List:", L)





