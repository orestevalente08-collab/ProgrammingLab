import random

class Coin():
    def __init__(self, faccia):
        self.faccia = faccia

    def faccia_attuale(self):
        return self.faccia

    def lancio(self):
        if random.randint(0, 1) == 0:
            self.faccia = "Testa"
        else:
            self.faccia = "Croce"

moneta = Coin ("Testa")
moneta.lancio()
print(moneta.faccia_attuale())