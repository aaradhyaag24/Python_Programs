numbers = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30, 6: 35, 7: 40, 8: 45, 9: 50, 10: 55}

print (numbers)

for key, value in list(numbers.items()):

    if value % 2 != 0:

        numbers.pop(key)

print ("after moving odd values:  ",numbers)

for key in numbers:

    numbers[key] = numbers [key] ** 2

print ("after squaring ",numbers)

numbers.update({11: 60, 12: 70, 13: 80})

print("After adding 3 pairs:", numbers)

numbers.popitem()

print("After removing last pair:", numbers)

sorted_dict = {}

for key in sorted(numbers):
    
    sorted_dict.update({key: numbers[key]})

print("Final dictionary:", sorted_dict)