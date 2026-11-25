n = int(input("enter number of elements "))

a = []

for i in range (n):

    m = int(input("enter number "))

    a.append (m)

print ("original list:", a)

element = int(input("enter element to be inserted "))

position = int(input("enter position "))

a.insert (position, element)

print ("list after changes ",a)