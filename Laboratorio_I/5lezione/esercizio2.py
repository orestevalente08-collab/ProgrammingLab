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
    
class NumericalCSVFile(CSVFile):

    def get_data(self):
        som = super().get_data()
        for line in som:
            for i in range(len(line)):
                try:
                    line[i] = float(line[i])
                except ValueError:
                    line[i] = line[i]
        return som

file = NumericalCSVFile("file", " ")
with open(r"3lezione\shampoo_sales.csv") as f:
    file.write(f)
    a = file.get_data()
    print(a)