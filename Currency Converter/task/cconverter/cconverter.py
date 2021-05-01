class CryptoCurrency:
    def __init__(self, name):
        self.name = name
        self.quantity = 0

    def __iadd__(self, quantity):
        self.quantity += quantity
        return self

    def greet(self):
        print(f'Meet a {self.name}!')

    def in_dollars(self):
        return self.quantity * 100

    def show(self):
        plural = self.quantity > 1
        name = self.name if not plural else self.name + 's'
        print(f'I have {self.quantity} {name}.',
              f'{self.quantity} {name} cost {self.in_dollars()} dollars.',
              'I am rich! Yippee!',
              sep='\n')


conicoin = CryptoCurrency("conicoin")
amount = int(input())
conicoin += amount
conicoin.show()
