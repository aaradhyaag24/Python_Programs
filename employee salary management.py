employees = {}

n = int(input("enter number of employees  "))

for i in range (n):

    id = input("enter employee id  ")

    salary = int(input("enter salary of employee  "))

    employees.update({"id" : salary})

print ("original dictionary ",employees)

for i in employees :

    employees[i] = employees[i] + (employees[i] * 10 /100)

print ("updated salaries   ",employees)

employees.setdefault("E100",30000)

print ("after adding new employees  ",employees)

min_salary = min(employees.values())

for key, value in list(employees.items()):

    if value == min_salary:

        employees.pop(key)

        print("Removed employee:", key)
        break

print("After removing minimum salary employee:", employees)

print("Employee IDs in sorted order:")

for key in sorted(employees):

    print(key, ":", employees[key])

max_salary = 0

min_salary = float('inf')

for key, value in employees.items():

    if value > max_salary:

        max_salary = value

        max_id = key

    if value < min_salary:

        min_salary = value

        min_id = key

print("Maximum salary:", max_id, max_salary)

print("Minimum salary:", min_id, min_salary)
