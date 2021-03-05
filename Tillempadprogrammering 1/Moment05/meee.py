class bankAccount():
    name = ''
    balance = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return self.balance
        else:
            pass