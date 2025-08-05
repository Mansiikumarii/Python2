class Account:
    def __init__(self,bal, acc):
        self.balance = bal
        self.account_number = acc

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Debited amount:", amount)
        print("New balance:", self.balance)

    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Credited amount:", amount)
        print("New balance:", self.balance)

    #get balance method
    def get_balance(self):
        return self.balance
    
acc1 = Account(35616109668232, 12345678901)

acc1.debit(37434048297154)
acc1.credit(1234567890123456)
acc1.debit(37434048297154)
acc1.credit(238492760158)