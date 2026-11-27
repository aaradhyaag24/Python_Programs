students_data = {}

n = int(input("enter no. of students  "))

for i in range (n):

    name = input("enter name of student   ")

    marks = int(input("enter marks of student   "))

    students_data.update({name : marks})

print ("students names   ",students_data.keys())

print ("students marks    ",students_data.values())

highest_marks = 0

lowest_marks = 100

for key, value in students_data.items():

    if value > highest_marks:

        highest_marks = value

        highest_name = key

    if value < lowest_marks:

        lowest_marks = value

        lowest_name = key

print("Highest marks:", highest_name, highest_marks)

print("Lowest marks:", lowest_name, lowest_marks)

print ("total students   ",len(students_data))

print ("sorted names    ",sorted(students_data))
