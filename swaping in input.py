x=int(input("first no."))
y=int(input("second no."))
z=int(input("third no."))
a=int(input("fourth no."))
print(x,y,z,a)
let=x
print("before swap",x,y,z,a)
x=a
a=let
sen=y
y=z
z=sen
print("after swap",x,y,z,a)
