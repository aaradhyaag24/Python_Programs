products = {}

n = int(input("enter number of elements   "))

for i in range (n):

    name = input("enter name of product  ")

    stock = int(input("enter stock quantity of the product   "))

    products.update({name : stock})

print ("original inventory   ",products)

products.update({"laptop" : 15, "mobile" : 10, "mouse" : 8})

print ("updated inventory", products)

for name in list (products.keys()):

    if products[name] == 0:

        products.pop(name)

print ("available inventory", products)

maximum_stock_products = max(products)

print ("product with maximum stock  ", max(products))


