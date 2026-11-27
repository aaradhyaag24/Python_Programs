students = {
    101: ("Aarav", "Delhi", [85, 90, 78, 92]),
    102: ("Riya", "Agra", [95, 88, 91, 89]),
    103: ("Kabir", "Delhi", [72, 80, 85, 76]),
    104: ("Ananya", "Jaipur", [90, 95, 89, 94]),
    105: ("Vivaan", "Agra", [65, 75, 80, 70]),
    106: ("Meera", "Jaipur", [88, 92, 96, 90]),
    107: ("Arjun", "Delhi", [91, 85, 90, 87]),
    108: ("Ishita", "Agra", [78, 82, 75, 80]),
    109: ("Reyansh", "Jaipur", [95, 90, 93, 98]),
    110: ("Saanvi", "Delhi", [84, 89, 86, 91])
}

for key, value in students.items():

    print (value[0])

total_marks = {}

for key, value in students.items():

    name = value[0]

    marks = value[2]

    total = 0

    for i in marks:

        total = total + i

    average = total / 4

    print(name, "Total:", total)

    print(name, "Average:", average)

    total_marks.update({key: total})

print("New dictionary:", total_marks)

highest = 0

topper = ""

for key, value in total_marks.items():

    if value > highest:

        highest = value

        topper = students[key][0]

print("Topper:", topper)

print("Highest Marks:", highest)

overall_total = 0

for key, value in total_marks.items():

    overall_total = overall_total + value

overall_average = overall_total / len(students)

print("Overall Average:", overall_average)

print("Students above overall average:")

for key, value in students.items():

    average = sum(value[2]) / len(value[2])

    if average > overall_average / 4:
        
        print(value[0])

