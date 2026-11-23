age = int(input("enter patient's age: "))
days = int(input("enter no. of days patient admitted: "))
room_type = input("enter type of patient's room (General/Private/ICU): ")
insurance = input("check whether patient has insurance (Yes/No): ")

if (room_type == "General") or (room_type=="general"):
    price = 2000
elif (room_type == "Private") or (room_type=="private"):
    price = 5000
elif (room_type == "ICU") or (room_type=="icu"):
    price = 10000

room_bill = price * days

if age >= 60:
    if (insurance == "Yes") or (insurance == "yes"):
        discount = room_bill * (30/100)
    else:
        discount = room_bill * (10/100)

if age < 60:
    if (insurance == "Yes") or (insurance== "yes"):
        discount = room_bill * (20/100)
    else:
        discount = room_bill * (0/100)

emergency = 0

if (room_type == "ICU") and (days > 7):
    emergency = 5000

bill = room_bill - discount + emergency

print("...HOSPITAL BILL...")
print("Room Bill", room_bill)
print("Emergency Care Charge", emergency)
print("Hospital Bill", bill)