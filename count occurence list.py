x = int (input("enter number of elements"))

number = []

for i in range (x):

    n = int (input("enter no."))

    number.append(n)

search = int(input("enter no. to search"))

count = number.count(search)

print ("no. of occurences ",count)