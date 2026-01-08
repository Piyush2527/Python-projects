#we have to show 
# Current balance: use module to show
# Want to withdrawal : use module to withdrwal
# Want to deposite : use module to deposite

nlist={'piyush':'1',
       'nishant':'2',
       'gupta':'3',
       'abc':'4'}


print("Please provide your Credentails:")
name=input("Enter your Name: ")
id=input("Enter your ID: ")

permisson=0
for ke,va in nlist.items():
    if (ke in name):
        if (id in va):
            print("\t\nAccess granted!")
            permisson=1
        elif (id not in va):
            print(f"Access Denied!!!, please check you id and password.")
        break
    else:
        print(f'Sorry! User not found')
        break
if permisson==1:
    while True:
        print('''\n..............................................................................................
\t\t\t\tPlease select from below operations
..............................................................................................
1. Current balance
2. Want to withdrawal
3. Want to deposite
4. Quit''')
        choice1=int(input(f"Enter your choice Mr/Mrs. {name} : "))
        if choice1==1:
            from Currentbalance import balance
            balance()
        elif choice1==2:
            from Currentbalance import withdrwal
            withdrwal()
        elif choice1==3:
            from Currentbalance import depo
            depo()
        elif choice1==4:
            print("Thank you! Quiting.....")
            break
        else:
            print("Wrong input! ")
else:
    print("Thank you!")


