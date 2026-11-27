marks = {}

n = int(input("Enter number of subjects: "))

for i in range(n):

    subject = input("Enter subject name: ")

    mark = int(input("Enter marks: "))

    marks.update({subject: mark})

print("Original dictionary:", marks)

for key, value in marks.items():

    print(key, ":", value)

highest = max(marks.values())

lowest = min(marks.values())

for key, value in marks.items():

    if value == highest:

        print("Highest marks:", key, value)

    if value == lowest:

        print("Lowest marks:", key, value)

total = sum(marks.values())

average = total / len(marks)

print("Average marks:", average)

new_marks = dict.fromkeys(marks.keys(), 0)

print("New dictionary:", new_marks)

new_marks.update(marks)

print("Updated dictionary:", new_marks)

print("Subjects in alphabetical order:")

for key in sorted(new_marks):
    
    print(key, ":", new_marks[key])


