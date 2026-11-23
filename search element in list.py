x = int(input("enter no. of element "))

number = []

for i in range (x):

    n= int(input("enter number "))

    number.append(n)

search = int(input("enter the number to search "))

if search in number:

   print("number found at index",number.index(search)+1)

else:

    print("number not found")


