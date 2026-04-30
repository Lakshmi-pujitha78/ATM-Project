from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00
def deposit():
    damt=float(input("Enter your deposit amount: "))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Account xxxxx123 credited with INR:{}".format(damt))
        print("Account xxxxx123 Balance after Deposit :{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter your withdraw amount: "))
    if(wamt<=0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InsuffFundError
    else:
        bal=bal-balwamt
        print("Account xxxxx123 credited with INR:{}".format(bal))
        print("Account xxxxx123 Balance after Withdraw :{}".format(bal))
def balenq():
    print("Account xxxxx123 balance :{}".format(bal))