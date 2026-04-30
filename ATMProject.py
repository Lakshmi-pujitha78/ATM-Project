import sys
from ATMExcept import DepositError,WithDrawError,InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
while(True):
    try:
        menu()
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDON'T ENTER -VE AND ZERO VALUE FOR DEPOSIT")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS VALUE FOR DEPOSIT")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDON'T ENTER -VE AND ZERO VALUE FOR WITHDRAW")
                except InSuffFundError:
                    print("\tUR ACCOUNT DOES NOT HAVE SUFFICIENT FUNDS--READ PYTHON NOTES")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS VALUE FOR withdraw")
            case 3:
                balenq()
            case 4:
                print("\tThx for using this project")
                sys.exit()
            case _:
                print("\tUr Selection of Operation is wrong-try again")
    except ValueError:
        print("\tDon't Enter alnumns,strs and symbols for Choice--try again")