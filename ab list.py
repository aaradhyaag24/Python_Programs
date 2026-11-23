n = int (input("enter number of elements"))
l = [0] * n
for i in range (n):
    l[i] = input ("enter number")
print (l)

n = int(input("enter number of elements "))
l = [""] * n
for i in range (n):
    l[i] = input("enter cities name ")
    print (l)

n = int(input("enter number of elements "))
sum = 0
l = [0]*n
for i in range (n):
    l[i] = int(input ("enter number "))
    sum = sum + (l[i])
print (l)
print ("sum",sum)