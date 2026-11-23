total_booked = 0
total_vacant = 0
max_bookings = 0
max_row = 0

for i in range(10):
    booked = 0
    vacant = 0

    print("Enter booking status for Row", i + 1)

    for j in range(12):
        status = int(input("Seat " + str(j + 1) + " (0 = Vacant, 1 = Booked): "))

        if status == 1:
            booked += 1
            total_booked += 1
        elif status == 0:
            vacant += 1
            total_vacant += 1
        else:
            print("Invalid status!")

    if booked > max_bookings:
        max_bookings = booked
        max_row = i + 1

    if vacant == 12:
        print("Row", i + 1, "is completely vacant.")

print("\n----- CINEMA SEAT REPORT -----")
print("Total Booked Seats:", total_booked)
print("Total Vacant Seats:", total_vacant)
print("Row with Maximum Bookings:", max_row)
print("Maximum Bookings in a Row:", max_bookings)