students_data = {}

n = int(input("enter no. of students  "))

for i in range (n):

    name = input("enter name of student   ")

    marks = int(input("enter marks of student   "))

    students_data.update({name : marks})

print ("students names   ",students_data.keys())

print ("students marks    ",students_data.values())

highest_marks = max(students_data)

lowest_marks = min(students_data)

print (highest_marks)

print (lowest_marks)

print ("total students   ",len(students_data))

print ("sorted names    ",sorted(students_data))