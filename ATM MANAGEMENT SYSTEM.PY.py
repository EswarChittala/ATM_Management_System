#### ......ATM MACHINE......
import time
from datetime import date
def atm():
    amount=5000
    deposite=0
    withdraw=0
    print("...WELCOME TO UNION BANK OF INDIA....")
    print("...Insert your card...")
    a=input("Enter one click on Yes/No : ")

    
    if a.lower()=="yes":
        static_pin=1234
        pin=int(input("ENTER YOUR 4 DIGIT PIN: "))
        amount=5000

        if len(str(pin))==4 and static_pin==pin:
           # while choice!=5:
                print("....MAIN MENU....") 
                print(" 1.deposite \n 2.withdraw \n 3.ministatement \n 4.balance_enq \n 5.pinchange ")
                
                option=int(input("SELECT YOUR OPTION: "))
                if option==1:
                    print(" Select Your Account Type:\n 1.savings \n 2.current ")
                    options=int(input("SELECT YOUR OPTION: "))
                    if options==1 or options==2:
                        deposite=int(input("ENTER THE AMOUNT: "))
                        if deposite % 100==0:
                            amount+=deposite
                            print("processing.....")
                            print("AMOUNT DEPOSITED SUCCESSFULLY:",deposite,"Rs")
                            print(date.today())
                            time.sleep(2)
                            print("YOUR TOTAL BALANCE:",amount,"Rs")
                            print("===THANK FOR VISITING===")
                        else:
                            print("Only multiples of 100 acceptable:")
                    else:
                        print("Enter correct option: ")
                    #RECEPIT CODE
                    r=int(input("Do you want recipt 0/1:"))
                    if r==1:
                        print("=======Reciept=========")
                        time.sleep(1)
                        print("Account number:********345")
                        print("Deposite amount:",deposite)
                        print("Account balance:",amount)
                        print("date:",date.today())
                        print("==Thank for visting==")
                    else:
                        print("Enter correct option:")
                    
                elif option==2:
                    withdraw=int(input("ENTER WITHDRAW AMOUNT: "))
                    if withdraw>amount:
                        print("INSUFFICENT BALANCE...... ")
                    elif withdraw >=200:
                        if withdraw % 100==0:
                            amount-=withdraw
                            print("processing.....")
                            time.sleep(2)
                            print("AMOUNT WITHDRAW SUCCESSFULLY:",withdraw,"Rs")
                            print("YOUR TOTAL BALANCE:",amount,"Rs")
                            print("THANKS FOR VISITING")
                            print("======================")
                        else:
                            print("Only multiples of 100 acceptable:")
                    else:
                        print("ENTER MINIMUM AMOUNT.....500RS")
                    r=int(input("Do you want recipt 0/1:"))
                    if r==1:
                        print("================")
                        print("Account number:********345")
                        print("withdraw amount:",withdraw)
                        print("Account balance:",amount)
                        print("date:",date.today())
                        print("==Thank for visting==")
                    else:
                        print("Enter correct option:")
                elif option==3:
                    print("===========ATM=========")
                    print("Your account Ministatement: ")
                    print("YOUR ACCOUNT BALANCE:",amount,"Rs")
                    print("THANKS FOR VISITING")
                    print("======================")
                elif option==4:
                    print("===========ATM=========")
                    print("YOUR ACCOUNT BALANCE:",amount,"RS")
                    print("THANKS FOR VISITING")
                    print("======================")

                elif option==5:    
                    old_pin=int(input("enter your old pin:"))
                    if pin==old_pin:
                        new_pin=int(input("enter your new pin:"))
                        print("Pin change successfully..")
                    else:
                        print("Incorrect pin")


                '''if option==6:
                    print("1.Continue\n2.Exit")
                    option=int(input("ENTER YOUR OPTION: "))
                    if option==1:
                        print("\n")
                    elif option==2:
                        exit()'''
    else:
        print(".....Thank for visiting.....")

atm()
es=int(input("do you want to continue 0/1:"))
if es==1:
    while es==1:
        atm()
        es=int(input("do you want to continue 0/1:"))
    
else:
    print("Thank For Visting")
    print("==Visit Again==")

    
