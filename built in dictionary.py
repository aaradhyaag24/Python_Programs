#keys

cities = {'c1' : "agra" , 'c2' : "delhi", 'c3' : "jaipur", 'c4' : "banglore"}

print (cities.keys())

#values 

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

print (num.values())

#items

objects = {'ob1' : "pen", 'ob2' : "table", 'ob3' : "chair", 'ob4' : "book" }

print (objects.items())

#get 

fruits = {'f1' : "apple", 'f2': "mango", 'f3' : "litchi", 'f4' : "kiwi"}

print (fruits.get("f3"))

#update 

place = {'p1' : "tajmahal", 'p2' : "india gate", 'p3' : "mariene drive"}

place.update({'p4' : 'bridge'})

print (place)

#pop

students = {'name' : "xyz", 'class' : 12, 'subject' : "computer", 'color' : "red"}

students.pop('color')

print (students)

#popitem

cities = {'c1' : "agra" , 'c2' : "delhi", 'c3' : "jaipur", 'c4' : "banglore"}

cities.popitem()

print (cities)

#clear 

cities = {'c1' : "agra" , 'c2' : "delhi", 'c3' : "jaipur", 'c4' : "banglore"}

cities.clear()

print (cities)

#copy

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

num.copy()

print (num)

#setdefault

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

num.setdefault('n0', 0)

print (num)

#fromkey

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

num.fromkeys(['n5'],0)

print (num)

#len

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

print (len(num))

#type

#len

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

print (type(num))

#str

#len

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

print (str(num))

#sorted

cities = {'c1' : "agra" , 'c2' : "delhi", 'c3' : "jaipur", 'c4' : "banglore"}

print (sorted(cities))

#min

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

print (min(num))

#max

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

print (max(num))

#any

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

print (any(num))

#all

num = {'n1' : 1, 'n2' : 2, 'n3' : 4, 'n4' : 5}

print (all(num))