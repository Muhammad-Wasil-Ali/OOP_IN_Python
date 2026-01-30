class Bank:
    def __init__(self,accNo,balance):
        self.accNo=accNo
        self.balance=balance
    
    
    def withdrawAmount(self,amount):
        if amount < 0 and amount>self.balance:
            raise ValueError("Invalid amount The transaction can't processed")
        
        self.balance-=amount
        
        print("Amount withdraw successfully")
        print(f"Your remaining balance is {self.getBalance()}")
        
        
    def depositAmount(self,amount):
        if amount<0:
            raise ValueError("Amount should be greater than 0")
        
        self.balance+=amount
        
        print("Amount deposited successfully")
        print(f"Your current balance is {self.getBalance()}")
        
    def getBalance(self):
        return self.balance
    
    
acc1=Bank(123,1000)

acc1.withdrawAmount(100)
acc1.depositAmount(1000)