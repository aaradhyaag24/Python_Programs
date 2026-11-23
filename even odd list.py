x = int(input("enter no. of elements"))

number = []

even = []

odd = []

for i in range (x):

    num = int(input("enter no. "))

    number.append(num)

    if (num % 2 == 0):

        num = even.append(num)

    else:

        num = odd.append(num)

print ("even list = ",even)

print ("odd list =",odd)