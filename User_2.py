import BankAccount as ba
class User:

    def __init__(self,name,emil, number_of_accounts=1):
        self.name = name
        self.emil = emil
        if number_of_accounts == 1 :
            self.account = ba.BankAccount()
        elif number_of_accounts > 1:
            self.accounts = {}
            for i in range(1, number_of_accounts+1):
                self.accounts[i] = ba.BankAccount()


# bonus section
    def make_deposit(self, amount, account_id=None):

        if account_id is None:
            self.account.deposit(amount)
            return self
        self.accounts.get(account_id).deposit(amount)
        return self

    def make_withdrawal(self, amount, account_id=None):
        if account_id is None:
            self.account.withdraw(amount)
            return self
        self.accounts.get(account_id).withdraw(amount)
        return self

    def display_user_balance(self, account_id=None):
        if account_id is None:
            self.account.display_account_info()
            return self
        self.accounts.get(account_id).display_account_info()
        return self





ahmed = User("ahmed","hshsjajaj")
omer = User("omer", "fjdj")
amal = User("amal", "ckkd")
ahmed2 = User("ahmed2", "ckkd", 2)

ahmed.make_deposit(150).make_deposit(150).make_deposit(150).make_withdrawal(150).display_user_balance()
omer.make_deposit(150).make_deposit(145).make_withdrawal(150).make_withdrawal(150).display_user_balance()
amal.make_deposit(150).make_withdrawal(10).make_withdrawal(10).make_withdrawal(20).display_user_balance()
ahmed2.make_deposit(150,1).make_deposit(150,2).make_withdrawal(50,1).make_withdrawal(100,2).display_user_balance(1).display_user_balance(2)
