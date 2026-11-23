amount=int(input("enter amount"))
membership=input("enter membership")
if amount>=5000 and membership=="gold": 
    print("30% discount")
elif amount>=3000 and membership=="silver":
    print("20% discount")
elif amount>=1500:
    print("10% discount")
else:
    print("no discount")