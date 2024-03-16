'''create an ATM machine'''
'''displaying remaining amount in ATM'''
'''authenicating user
if the user is authenicated then give him the following options to choose 
1.check balance,2.cash withdrawal(rupay-2000 only\visa-50000\mastercard-8499),3.cash deposit'''#automatic balance should be displayed
'''mini stmts of the last 3 transactions'''
'''select 3 options of account:1.Rupay\2.Visa\3.Mastercard'''

class ATM:
    class authenicate:
        def authenicate(self):
            token=0
            name=input("enter your name:")
            password=input("enter your password:")
            if name==password:
                token=1
                print("authenication successful!!")
            else:
                print("authenication failure!!")
            return token
    
    def display(self):
        token=self.authenicate()
        if token==1:
            print("choose one of the options given below:")
            n=input(("1.check balance\2.cash withdrawal\3.cash deposit"))
            n=n.lower()
            return token
            if n=="check balance" or n=="1":
                print("remaining amount..")
            elif n=="cash withdrawal" or n=="2":
                print("choose one of the options given below:")
                n=input(("1.rupay\2.visa\3.mastercard"))
                n=n.lower()
                if n=="rupay" or n=="1":
                    print("only 2000₹ could be withdrawn at a time:")
                elif n=="visa" or n=="1":
                    print("only 5000₹ could be withdrawn at a time:")
                else:
                    print("only 8499₹ could be withdrawn at a time:")
            else:
                print("amount debited!!")
#t1=check_balance()
#t2=cash_withdrawal()
#t3=cash_deposit()
#t1.transaction_1(input("enter amount:"))
#t2.transaction_2(input("enter amount:"))
#t3.transaction_3(input("enter amount:"))

                
            

        


