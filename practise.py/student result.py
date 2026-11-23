sub1=int(input("marks of subject1"))
sub2=int(input("marks of subject2"))
sub3=int(input("marks of subject3"))
total=sub1+sub2+sub3
percentage=total/3
if sub1<33 or sub2<33 or sub3<33:
    print("fail")
elif percentage>=75:
    print("first division")
elif percentage>=60:
    print("first division")
elif percentage>=45:
    print("second division")
else:
    print("pass")

