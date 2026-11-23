for city in range (1,4):
    total = 0
    print ("enter temprature for city",city)
    for day in range(1,8):
        temp = float(input("enter temprature for day"))
        total = total + temp
        average = total/7
        print ("average temprature of city",city,"=",average)