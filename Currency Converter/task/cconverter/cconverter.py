class CryptoCurrency:
    def __init__(self, name):
        self.name = name
        self.quantity = 0
        self.rate = 0

    def __iadd__(self, quantity):
        self.quantity += quantity
        return self

    def set_quantity(self):
        self.quantity = int(input(f"Please, enter the number of {self.name}s you have: "))

    def set_rate(self):
        self.rate = float(input("Please, enter the exchange rate: "))

    def greet(self):
        print(f'Meet a {self.name}!')

    def in_dollars(self):
        return self.quantity * self.rate

    def show(self):
        plural = self.quantity > 1
        name = self.name if not plural else self.name + 's'
        print(f'I have {self.quantity} {name}.',
              f'{self.quantity} {name} cost {self.in_dollars()} dollars.',
              'I am rich! Yippee!',
              sep='\n')


conicoin = CryptoCurrency("conicoin")
conicoin.set_quantity()
conicoin.set_rate()
print(f'The total amount of dollars: {conicoin.in_dollars()}')
