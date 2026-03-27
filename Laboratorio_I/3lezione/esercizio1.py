class Veicolo:
    def __init__(self, modello, marca, anno, speed):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = speed

    def __str__ (self):
        return (f"modello: {self.modello}\n, marca: {self.marca}\n, anno: {self.anno}\n, speed: {self.speed}\n")
    
    def accellerare (self):
        self.speed += 5
    
    def frenare (self):
        self.speed -= 5
    
    def get_speed(self):
        return self.speed