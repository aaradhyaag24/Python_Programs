amount=float(input("enter purchase amount:"))
membership=input("enter type of membership (Premium / Regular):")
location=input("enter location:")
payment_method=input("enter method of payment (Online / COD):")

if (amount>=5000):
    if (membership.casefold=="premium"):
        discount= amount * (20 /100)
    elif (membership.casefold=="regular"):
        dicount= amount * (10/100)
    else:
        dicount=0

if (amount>=2000) and (amount<=4999):
    if (membership.casefold=="Premium"):
        dicount= amount * (10/100)
    elif (membership.casefold=="Regular"):
        discount= amount *(5/100)
    else:
        discount= 0

amount_after_discount= amount - discount

if (location.casefold=="local"):
    if (payment_method.casefold=="Online"):
        delivery=  00
    elif (payment_method.casefold=="COD"):
        delivery=  50

if (location.casefold=="outside"):
    if (payment_method.casefold=="Online"):
        delivery=  100
    elif (payment_method.casefold=="COD"):
        delivery= 200

final_amount= amount_after_discount + delivery

print("....BILL....")
print("discount=,discount")
print("delivery=,delivery")
print("final_amount=,final_amount")


                
           


        
         






