class CSVFile:
    def __init__(self, name, contenuto):
        self.name = name + ".csv"
        self.contenuto = contenuto

    def write(self, added):
        self.contenuto = added
        

    def get_data(self):
        try:
            self.contenuto = open(self.name, 'r')
            som = []
            for line in self.contenuto:
                som.append(line.split(','))
            file.close()
            return som
        except FileNotFoundError:
            print('File non trovato\n')

file = CSVFile(r"C:\Users\orest\Documents\Programmazione\Python\ProgrammingLab\3lezione\shampoo_sales", " ")
a = file.get_data()
print(a)