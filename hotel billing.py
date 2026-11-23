nights = float(input("enter no. of nights: "))
room_type = input("enter type of room(Standard/Deluxe/Suite): ")
membership = input("enter membership (Gold/Silver/None): ")
weekend_stay = input("enter if stayed on weekend (Yes/No): ")
guests = int(input("enter no. of guests: "))

if room_type.casefold() == "Standard":
    price = 2500
elif room_type.casefold( )== "Deluxe":
    price = 4000
elif room_type.casefold() == "Suite":
    price = 7000
else:
    price = 0

room_bill = price * nights

discount = 0

if nights > 5:
    if membership.casefold() == "Gold":
        discount = room_bill * (20/100)
    elif membership.casefold() == "Silver":
        discount = room_bill * (10/100)
    else:
        discount = room_bill * (5/100)

weekend_charge = 0

if weekend_stay.casefold() == "Yes":
    weekend_charge = 100

guest_charge = 0

if guests > 2:
    guest_charge = (guests - 2) * 500 * nights

final_amount = room_bill - discount + guest_charge + weekend_charge

print("...BILL...")
print("Room Type:", room_type)
print("Room Bill:", room_bill)
print("Discount:", discount)
print("Weekend Charge:", weekend_charge)
print("Extra Guest Charge:", guest_charge)
print("Final Amount:", final_amount)