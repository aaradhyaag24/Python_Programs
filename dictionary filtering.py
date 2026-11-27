dictionary = {}

n = int(input("enter number of names you want "))

for i in range (n):

    name = input("enter name  ")

    age = int(input("enter age "))

    dictionary.update({name : age})

print (dictionary)

adults = {}

for key, value in dictionary.items():

    if value >= 18:

        adults.update({name : age})

print ("people aged 18 or above ",adults)

minors = {}

for key, value in dictionary.items():

    if value <= 18:

        minors.update({name : age})

print ("total number of peple in adults  ", len(adults))

print ("total number of people in minors  ", len(minors))

oldest = 0

youngest = 100 

for key, value in dictionary.items():

    if value > oldest:

        oldest = value 

        oldest_name = key

        if value < youngest:

            youngest = value 

            youngest_name = key 

print ("oldest person  ", oldest_name, oldest)

print ("youngest person  ",youngest_name, youngest)

sorted_names = sorted(dictionary)

print ("names in alphabetical order ")

for name in sorted_names:

    print (name)

