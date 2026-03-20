class CSVFile:
    def __init__(self, name, contenuto):
        if not isinstance(name, str):
            print("Il nome non è una stringa")
        else:
            self.name = name + ".csv"
            self.contenuto = contenuto

    def write(self, added):
        self.contenuto = added

    def get_data(self, s, end):
        som = []
        if (s>end):
            print("L'inizio non può essere maggiore della fine\n")
        else:
            for i, line in enumerate(self.contenuto):
                if i>=s and i <= end:
                    som.append(line.split(','))
        return som

file = CSVFile("file", " ")
with open(r"C:\Users\orest\Documents\Programmazione\Python\ProgrammingLab\3lezione\shampoo_sales.csv") as f:
    file.write(f)
    a = file.get_data(4, 6)
    print(a)