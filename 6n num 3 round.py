for i in range(1, 4):

    positive = 0
    negative = 0
    zero = 0

    print("Round", i)

    for j in range(1, 7):

        num = int(input("Enter number: "))

        if num > 0:
            positive = positive + 1

        elif num < 0:
            negative = negative + 1

        else:
            zero = zero + 1

    print("Positive numbers:", positive)
    print("Negative numbers:", negative)
    print("Zero numbers:", zero)