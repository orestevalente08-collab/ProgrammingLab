#Oreste Valente SM32A00011

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):

        try:    #provo ad aprire il file per vedere se esiste

            f = open(name, 'r')

        except FileNotFoundError: raise ExamException("File not Found\n")

        f.close()

        self.name = name

    def get_data(self):

        data = []   #inizializzo una lista vuota

        with open(self.name, 'r') as f: #provo ad aprire il file

            next(f) #salto header

            for line in f:
                line = line.strip() #tolgo gli spazi e i \n
                line = line.split(',')    #divide le righe usando come separatore la ,

                try:    #provo a convertire la seconda e la terza colonna in float
                    line[1] = float(line[1])
                    line[2] = float(line[2])
                except ValueError:  #se non riesce a convertire continua il codice
                    print("Not valid value\n")
                    continue

                if line[2] < 5:
                    data.append(line)   #controlla che la variazione sia minore di 5
                else:
                    print("Valore troppo incerto\n")

            return data


def compute_month_variation(time_series, first_year, second_year):

    T_first_year = {}   #dizionario con le temperature del primo anno divise per mese

    T_second_year = {}  #dizionario con le temperature del secondo anno divise per mese

    for line in time_series:

        line[0] = line[0].split("-")    #divido anno e mese

        line[0][0] = int(line[0][0])    #converto anno e mese in interi
        line[0][1] = int(line[0][1])

        if line[0][0] == first_year:

            T_first_year[line[0][1]] = line[1]  #salvo le temperature nel dizionario

        elif line[0][0] == second_year:

            T_second_year[line[0][1]] = line[1] #salvo le temperature nel dizionario

    


    variations = {}

    for idx in range(1, 13):
        try:  #calcola la differenza dei valori per lo stesso mese e la salva in un dizionario
            variations[idx] = T_first_year[idx] - T_second_year[idx]

        except Exception:
            print("Mancano dei mesi\n")

    if variations == {}: raise ExamException("Gli anni non hanno mesi in comune\n")

    return variations




time_series_file = CSVTimeSeriesFile("Temperatures.csv")
time_series = time_series_file.get_data()
print(time_series)
variations = compute_month_variation(time_series, 1900, 2000)
print(variations)
