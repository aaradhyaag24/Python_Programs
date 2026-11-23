print("TECH HUB")

registration_fee = 500

print("COURSES OFFERED AND FEE")

python_programming = 6000
java_programming = 8000
cplus_programming = 5000
web_programming = 10000
data_analytics = 12000

print("NUMBER OF STUDENTS")
n = int(input("ENTER NO. OF STUDENTS: "))

for i in range(1, n + 1):

    print("STUDENT", i, "ADMISSION")

    print("STUDENTS INFO")

    student_id = input("ENTER STUDENT ID: ").casefold()

    name = input("ENTER NAME OF STUDENT: ").casefold()

    age = int(input("ENTER AGE OF STUDENT: "))

    if (age < 15):
        print("AGE NOT VALID")
        continue

    mobile = int(input("ENTER MOBILE NUMBER: "))

    if (mobile <10):
        print("INVALID MOBILE NUMBER")
        continue

    percentage = int(input("ENTER PREVIOUS EXAMINATION PERCENTAGE: "))

    if (percentage < 0) or (percentage > 100):
        print("INVALID PERCENTAGE")
        continue

    print("COURSE SELECTION")
    print("1. Python Programming = 6000/-")
    print("2. Java Programming = 8000/-")
    print("3. C++ Programming = 5000/-")
    print("4. Web Development = 10000/-")
    print("5. Data Analytics = 12000/-")

    course = int(input("ENTER COURSE NO.: "))

    if course == 1:
        course_name = "Python Programming"
        course_fee = python_programming

    elif course == 2:
        course_name = "Java Programming"
        course_fee = java_programming

    elif course == 3:
        course_name = "C++ Programming"
        course_fee = cplus_programming

    elif course == 4:
        course_name = "Web Development"
        course_fee = web_programming

    elif course == 5:
        course_name = "Data Analytics"
        course_fee = data_analytics

    else:
        print("INVALID COURSE")
        continue

    print("DISCOUNTS OFFERED")

    if percentage >= 90:
        discount = 15

    elif percentage >= 80:
        discount = 10

    elif percentage >= 70:
        discount = 5

    else:
        discount = 0

    discount_amount = course_fee * (discount / 100)

    months = int(input("ENTER NO. OF MONTHS: "))

    total_fee = course_fee * months

    discount_amount = total_fee * (discount / 100)

    final_payable_amount = total_fee - discount_amount + registration_fee

    print(".....ADMISSION RECEIPT.....")
    print("STUDENT ID:", student_id)
    print("STUDENT NAME:", name)
    print("AGE:", age)
    print("MOBILE:", mobile)
    print("PERCENTAGE:", percentage)
    print("COURSE:", course_name)
    print("MONTHS:", months)
    print("COURSE FEE:", course_fee)
    print("TOTAL FEE:", total_fee)
    print("DISCOUNT:", discount, "%")
    print("DISCOUNT AMOUNT:", discount_amount)
    print("REGISTRATION FEE:", registration_fee)
    print("FINAL PAYABLE AMOUNT:", final_payable_amount)

print("..INSTITUE REPORTS..")

print("LIST OF REGISTERED STUDENTS:")

n=int(input("ENTER N:"))

for i in range (1,n+1):
    print(i)



