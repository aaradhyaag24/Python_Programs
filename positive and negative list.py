x = int(input("enter no. of elements "))

number = []

positive = []

negative = []

zero = []

for i in range (x):

    num = int (input("enter no. "))

    number.append(num)

    if (num > 0):

        positive.append(num)

    elif (num < 0):

        negative.append(num)

    else:

        print ("zero")

print ("positive list =",positive)

print ("negative list =",negative )

print ("zero list = ",zero)
