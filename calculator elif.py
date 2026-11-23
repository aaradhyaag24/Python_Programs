x=int(input("value "))
y=int(input("value "))
print("value of","x","y")
operations= input("operations")
print("+")
print("-")
print("*")
print("%")
print("/")
if operations=="+":
    print("ans= ",x+y)
elif operations=="-":
    print("ans= ",x-y)
elif operations=="*":
    print("ans= ",x*y)
elif operations=="%":
    print("ans= ",x%y)
elif operations=="/":
    print("ans=",x/y)
else:
    print("no output")