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

