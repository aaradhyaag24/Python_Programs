cities = []

n = int(input("enter number of cities you want "))

for i in range (n):

    name = input("enter city name ")

    population = int(input("enter population of the city  "))

    cities.update({"name" : population})