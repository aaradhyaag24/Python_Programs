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

highest_stock = 0

for key, value in products.items():

    if value > highest_stock:

        highest_stock = value

        highest_product = key

print("Maximum stock product:", highest_product, highest_stock)

print("Products having stock less than 10")

for key, value in products.items():

    if value < 10:

        print(key, value)

print("Total available products:", len(products))

for name in list(products.keys()):

    if products[name] == 0:
        
        products.pop(name)
