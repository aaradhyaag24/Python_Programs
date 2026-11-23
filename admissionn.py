age=int(input("enter age"))
percentage=input("enter percentage")
if age>=17 and age<=25:
    if percentage>=75:
        print("eligible for merit")
    else:
        print("eligible for regular admission")
else:
    print("not eligible")

