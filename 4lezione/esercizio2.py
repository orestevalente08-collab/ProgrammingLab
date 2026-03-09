class Veicolo:
    def __init__(self, modello, marca, anno, speed):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = speed

    def __str__ (self):
        return (f"modello: {self.modello}\n marca: {self.marca}\n anno: {self.anno}\n speed: {self.speed}\n")
    
    def accellerare (self):
        self.speed += 5
    
    def frenare (self):
        self.speed -= 5
    
    def get_speed(self):
        return self.speed

class auto(Veicolo):
    def __init__(self, modello, marca, anno, speed, numero_porte):
        super().__init__(modello, marca, anno, speed)
        self.numero_porte = numero_porte
    
    def __str__(self):
        return f"modello: {self.modello}\n marca: {self.marca}\n anno: {self.anno}\n speed: {self.speed}\n numero porte: {self.numero_porte}\n"
    

class moto(Veicolo):
    def __init__(self, modello, marca, anno, speed, tipo):
        super().__init__(modello, marca, anno, speed)
        self.tipo = tipo

    def __str__(self):
        return f"modello: {self.modello}\n marca: {self.marca}\n anno: {self.anno}\n speed: {self.speed}\n tipo: {self.tipo}\n"

a = auto("TT", "Audi", 1980, 0, 4)
m = moto("C4", "Ducati", 2001, 0, "Touring")
print(a)
print(m)