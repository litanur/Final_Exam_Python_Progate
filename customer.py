from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance

    def cekId(self):
        return self.id
    
    def cekPin(self):
        return self.pin
    
    def cekSaldo(self):
        return self.balance

    def withDrawBalance(self, amount):
        self.balance -= amount

    def depositBalance(self, amount):
        self.balance += amount