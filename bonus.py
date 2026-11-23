years=int(input("no. of years worked"))
salary=int(input("enter salary"))
if years>=2:
    if salary>=50000:
        bonus=salary*(15/100)
        totalbonus = bonus + salary
        print("bonus==",bonus)
        print("Total Salary==",totalbonus)
    else:
        bonus=salary*10/100
        totalbonus= bonus + salary
        print("total salary==",totalbonus)
else:
    print("no bonus")
