cities = {}

n = int(input("Enter number of cities you want "))

for i in range(n):

    name = input("Enter city name ")

    population = int(input("Enter population of the city "))

    cities.update({name: population})

print("Original dictionary:", cities)

max_population = 0

min_population = 100000000

for key, value in cities.items():

    if value > max_population:

        max_population = value

        max_city = key

    if value < min_population:

        min_population = value

        min_city = key

print("City with maximum population:", max_city, max_population)

print("City with minimum population:", min_city, min_population)

top5_cities = sorted(cities, key=cities.get, reverse=True)[:5]

print("Top 5 cities:")

for key in top5_cities:

    print(key, cities[key])

for key in list(cities.keys()):

    if cities[key] < 500000:

        cities.pop(key)

print("Modified dictionary:", cities)

copied_cities = cities.copy()

print("Copied dictionary:", copied_cities)

cities.update({"Agra": 1800000})

print("Original dictionary after adding new city:", cities)

if "Agra" in copied_cities:

    print("Agra exists in copied dictionary")

else:

    print("Agra does not exist in copied dictionary")
