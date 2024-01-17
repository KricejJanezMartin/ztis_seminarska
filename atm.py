class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.card_inserted = False
        self.account = None

    def insert_card(self, card, account):
        if card.is_valid:
            self.card_inserted = True
            self.account = account
        else:
            self.card_inserted = False
        return self.card_inserted

    def request_money(self, amount):
        if self.balance >= amount and self.card_inserted:
            withdrawn = self.account.withdraw(amount)
            if withdrawn > 0:
                self.balance -= withdrawn
            return withdrawn
        else:
            return 0

    def return_card(self):
        if self.card_inserted:
            self.card_inserted = False
            self.account = None
            return True
        else:
            return False