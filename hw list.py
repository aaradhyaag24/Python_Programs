x = int(input("enter no. of elements "))

number = []

for i in range (x):

    n = int(input("enter a number"))

    number.append (n)

unique = []

for i in number:

    if i not in unique:

        unique.append(i)

print ("original list:", number)

print("Unique elements:", unique)