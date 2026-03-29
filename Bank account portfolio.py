class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    
    def debit(self,amount):
        self.balance-=amount
        print("Rs", amount, "is debited from account")
        print("remaning bal is:",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited")
        print("your balance is:", self.get_balance(),acc1.accno)

    def get_balance(self):
        return self.balance

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
