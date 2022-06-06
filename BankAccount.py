

class BankAccount:
    def __init__(self, balance=0, int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        elif self.balance < amount:
            self.balance -= 5
            print( "Insufficient funds: Charging a $5 fee" )
            return self
        return self

    def display_account_info(self):
        print("Balance:",self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0 :
            self.balance = self.balance + (self.balance * self.int_rate)
            print(self.balance)
            return self



acount1 = BankAccount()
acount2 = BankAccount()
print("account 1:")
acount1.deposit(120).deposit(110).deposit(130).withdraw(2000).yield_interest().display_account_info()
print("account 2:")
acount2.deposit(20).deposit(90).withdraw(32).withdraw(23).withdraw(9).withdraw(23).yield_interest().display_account_info()


