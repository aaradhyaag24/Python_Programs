age=int(input("enter age:"))
price=int(input("enter price of ticket:"))
flyclass=input("enter type of class(Economy / Business):")
membership=input("enter type of membership(Gold/Silver/None):")
type=input("enter travel type(Domestic/International):")

if (age<12):
    discount = 50
elif (age>=60):
    discount = 30
else:
    discount = 00

price = price - (price * discount /100)

if (membership.casefold=="Gold"):
    discount = 15
elif (membership.casefold=="Silver"):
    discount = 10
else:
    discount = 00

if (flyclass.casefold=="Business"):
    if (type=="International"):
        price = price + 5000
    elif (type=="Domestic"):
            price = price + 2000

if (flyclass.casefold=="Economy"):
    if (type=="International"):
                price = price + 2000
    elif (type=="Domestic"):
            price = price + 00

print("final ticket price:",price)


                

            