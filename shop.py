amount = int(input("Enter amount: "))
premium = input("Premium yes or no: ")

if amount >= 3000:
    if premium == "yes or YES":
        discount = amount * (20/100)
        totaldiscount = amount - discount
        print("Total amount =", totaldiscount)
    else:
        discount = amount * (10/100)
        totaldiscount = amount - discount
        print("Total amount =", totaldiscount)
else:
    print("No discount")

