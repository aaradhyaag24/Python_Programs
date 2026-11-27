dictionary = {}

n = int(input("enter number of elements  "))

for i in range (n):

    name = input("enter name  ")

    age =int(input("enter age  "))

    dictionary.update({"name",age})

adults = {}

minors = {}

for name, age in dictionary.items();

    if age 