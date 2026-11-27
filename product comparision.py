product = {}

n = int(input("enter number of products you want "))

for i in range (n):

    name = input("enter product name you want ")

    price = int(input("enter price "))

    product.update({name : price})

print (product)

common = {}

for key in product:

    if key in product :

        common.update({key:product[key]})

print ("common products ",common)

only_first = {}

for key in product:

    if key not in product:

        only_first.update({key: product [key]})

print("Only in first:", only_first)

only_second = {}

for key in product:

    if key not in product :

        only_second.update({key: product [key]})

print("Only in second:", only_second)




