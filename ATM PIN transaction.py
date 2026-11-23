pin = int(input("Enter PIN: "))
balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))
account_type = input("Enter account type (Savings/Current): ")

if (pin == 1234):

    if (withdrawal <= 0):
        print("Transaction Failed")

    elif (account_type.casefold() == "Savings") and (balance - withdrawal >= 1000):
        balance = balance - withdrawal
        print("Transaction Successful")
        print("Remaining Balance:", balance)

    elif (account_type.casefold() == "Current") and (withdrawal <= balance + 5000):
        balance = balance - withdrawal
        print("Transaction Successful")
        print("Remaining Balance:", balance)

    else:
        print("Transaction Failed")

else:
    print("Incorrect PIN")
        



        