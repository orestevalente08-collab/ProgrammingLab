class canguro:
    def __init__(self):
        self.contenuto_tasca = []
    
    def intasca(self, x):
        self.contenuto_tasca.append(x)

    def __str__(self):
        return f"Canguro con tasca: {self.contenuto_tasca}"

c = canguro()
c.intasca('missile')
print(c)