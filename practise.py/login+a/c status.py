username=input("enter username")
password=int(input("enter password "))
verified=input("account verified")
if "username"=="aaradhya.243" and "password"=="12345" and "verified"=="account verified":
    print("login successful")
elif "username"=="aaradhya.243" and "password"=="12345" and "verified"=="account unverified":
    print("verify your account")
else:
    print("invalid credentials")