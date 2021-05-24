class CryptoCurrency:
    def __init__(self, name):
        self.name = name
        self.quantity = 0.0
        self.rate = dict()

    def __iadd__(self, quantity):
        self.quantity += quantity
        return self

    def set_quantity(self):
        self.quantity = float(input())

    def set_rate(self, currency, rate):
        self.rate[currency] = rate

    def show_currencies(self):
        plural = self.quantity > 1.0
        name = self.name if not plural else self.name + 's'
        for currency, rate in self.rate.items():
            print(f'I will get {round(self.quantity * rate, 2)} {currency} from the sale of {self.quantity} {name}.')


conicoin = CryptoCurrency("conicoin")
conicoin.set_quantity()
conicoin.set_rate("RUB", 2.98)
conicoin.set_rate("ARS", 0.82)
conicoin.set_rate("HNL", 0.17)
conicoin.set_rate("AUD", 1.9622)
conicoin.set_rate("MAD", 0.208)
conicoin.show_currencies()
