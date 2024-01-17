class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount # Successful withdrawal
        else:
            return 0 # Not enough money