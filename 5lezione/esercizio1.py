class CSVFile:
    def __init__(self, name, contenuto):
        self.name = name + ".csv"
        self.contenuto = contenuto

    def write(self, added):
        self.contenuto = added
        

    def get_data(self):
        som = []
        for line in self.contenuto:
            som.append(line.split(','))
        return som
    
file = CSVFile("file", " ")
try:
    with open(r"C:\Users\orest\Documents\Programmazione\Python\ProgrammingLab\3lezione\shampoo_sales.csv") as f:
        file.write(f)
        a = file.get_data()
        print(a)
except FileNotFoundError:
    print("Il file richiesto non esiste\n")