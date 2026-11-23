for i in range (1,5):

    present = 0

    absent = 0

    print ("class",i)

    for j in range (1,11):

        attendance = int (input("enter attendance(1 = present, 0 = absemt)"))

        if (attendance == 1):
            present = present + 1

        elif (attendance == 0):
            absent = absent + 1

    print ("total present students ", present)
    print ("total absent", absent)


