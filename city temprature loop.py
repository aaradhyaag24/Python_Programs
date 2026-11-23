for i in range (1,4):

    city = input("enter city name ")

    total = 0

    for j in range (1,8):

        temp = float (input("enter temprature of the day" + str(j)))

        total = total + temp

        average =total / 7

    print ("average temprature",average)