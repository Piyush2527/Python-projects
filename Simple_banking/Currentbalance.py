
fsum=1000
def balance():
    global fsum
    print(f"Current balance is: {fsum}")

def depo():
    global fsum
    moneydepo=int(input("Please enter the amount that you want to deposite: "))
    print(f'You have successfully added: {moneydepo}')
    fsum+=moneydepo
    

def withdrwal():
    global fsum
    moneydraw=int(input("Please enter the amount that you need to withdraw: "))
    if moneydraw<=fsum:
        print(f'You have successfully withdrawal: {moneydraw}')
        fsum-=moneydraw
        # balance(fsum)
    else:
        print(f'Sorry! Insufficient balance')
        # balance(fsum)



if __name__== '__main__':
    print('''You are inside Cuurent balance module
          where you have current money in your account''')