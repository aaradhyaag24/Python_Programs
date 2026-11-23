#len
a = [1,2,3,4,5,6,7]

print (len(a))

#max and min
a = [59,29,48,90]

print (max(a))
print (min(a))

#sorted
a = [4,3,9,7,5,11]

print (sorted(a))

#sum
a = [3,18,22,56,78]

print (sum(a))

#list
a = ("ABC")
b = ("123")

print(list(a))
print(list(b))

#any
a =[0,-1,5]

print (any(a))

b = [0,0,0]

print (any(b))

#all
a = [1,2,3,4]

print (all(a))

b = [0,1,2,3]

print (all(b))

#reversed
a = [1,2,3,4,5]

print (list(reversed(a)))

#enumerate 
a = ['1','2','3','4']

print(list(enumerate(a)))

#append
a = [1,2,3,4]
a.append (5)

print (a)

#extend 
a = [1,2,3,4]
a.extend([5,6,7,8])

print (a)

#insert
a = ["apple","banana","cherry"]
a.insert(4, "orange")

print(a)

#remove 
a = ["bat","cat","dog"]
a.remove("bat")

print(a)

#pop
a = ["bat","cat","dog"]
a.pop(1)

print(a)

#clear
a = [1,2,3,4,5]
a.clear()

print (a)

#index
a = [1,2,3,4,5,6,7,8]

print(a.index(5))

#count
a = [1,2,2,3,4,5,5,5,6]

print(a.count(5))

#reverse 
a = [3,2,1,4,6]
a.reverse()
print (a)

#sort
a = [3,2,5,1,6,4]
a.sort()

print(a)

#copy
a = [1,2,3,4,5]
b = a.copy()

print (b)