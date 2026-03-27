class Poligono:
    def __init__ (self, lati):
        self.lati = lati
    
    def __str__(self):
        return f"Sono un poligono con {self.lati} lati"
    
class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)
    
    def __str__(self):
        return "Sono un quadrilatero"
    
class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
    
    def __str__(self):
        return super().__str__() + "\nSono un rettangolo"
    
    def perimetro(self):
        return self.base*2 + self.altezza*2
    
    def area(self):
        return self.base * self.altezza
    
class Triangolo(Poligono):
    def __init__(self, lato1, lato2, lato3):
        super().__init__(3)
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3
    
    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3
    
    def is_equilatero(self):
        if self.lato1 == self.lato2 == self.lato3:
            return True
        else:
            return False
