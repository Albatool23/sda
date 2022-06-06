
class User:

    def __init__(self,name,emil):
        self.name = name
        self.emil = emil
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self





ahmed = User("ahmed","hshsjajaj")
omer = User("omer", "fjdj")
amal = User("amal", "ckkd")

ahmed.make_deposit(150).make_deposit(150).make_deposit(150).make_withdrawal(150).display_user_balance()
omer.make_deposit(150).make_deposit(145).make_withdrawal(150).make_withdrawal(150).display_user_balance()
amal.make_deposit(150).make_withdrawal(10).make_withdrawal(10).make_withdrawal(20).display_user_balance()

