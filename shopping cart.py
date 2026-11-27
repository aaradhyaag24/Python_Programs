cart = {}

n = int(input("enter number of items  "))

for i in range (n):

    name = input("enter name of the item  ")

    price = int(input("enter price of the item  "))

    cart.update({"name" : price})

update_cart = cart.update({"pen" : 20, "towels" : 6})

print ("updated items  ",update_cart)

pop_item = cart.popitem()

print ("remove recently added item ",pop_item)

copy_cart = cart.copy()

print ("copy of the cart  ",copy_cart)

clear_cart = copy_cart.clear()

print ("copied cart after clear  ",clear_cart)

total_items = len(cart)

print ("total number of items in the cart  ",total_items)






