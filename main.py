import sys
class Bank:
    def inputdata(self):
        self.acname=input("Customer name")
        self.passw=int(input("Enter Password"))
        self.acno=int(input("Enter account no"))
        self.bal=int(input("Enter balance"))
    def deposit(self):
        amt=int(input("Enter the ammount"))
        self.bal=self.bal+amt
    def withdraw(self):
        amt=int(input("Enter the ammount"))
        self.bal=self.bal-amt
    def displaybalance(self):
        print("Account no",self.acno)
        print("Account balance",self.bal)
cust=Bank()  
while True:
    print("-"*30)
    print("Customer Account details")
    print("1.Account Holder Name")
    print("2.Enter password")
    print("3.Deposite Ammount")
    print("4.Withdraw")
    print("5.Display Balance")
    print("6.Exit")
    print("-"*30)
    choice=int(input("Enter your choice"))
    if choice==1:
        cust.inputdata()
    elif choice==2:
        cust.deposit()
    elif choice==3:
        cust.withdraw()
    elif choice==4:
        cust.displaybalance()
    elif choice==5:
             pass
    elif choice==6:
        sys.exit()
                    
            
        