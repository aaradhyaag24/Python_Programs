x = int(input("enter no. of elements  "))

number = []

for i in range (x):

    n = int(input ("enter the no. "))

    number.append(n)

largest_num = number[0]

second_largest = number[0]

for i in number :

    if (i > largest_num):

        second = largest_num

        largest = i

    elif (i > second):

        second = i

print ("second largest number ",second)