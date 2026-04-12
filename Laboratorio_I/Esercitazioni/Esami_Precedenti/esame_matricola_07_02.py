class ExamException(Exception): #per sollevare errori
    pass


class CSVTimeSeriesFile:

    def __init__(self, name):
        try:    #provo ad aprire il file per vedere se esiste
            f = open(name, 'r')

        except FileNotFoundError:   #se non esiste alza un errore
            raise ExamException("ERROR: File not Found\n")
        
        f.close()   #chiudo il file se esiste

        self.name = name    #aggiungo l'attributo name



    def get_data(self):

        temperatures = []   #lista dovve salvo i valori delle temperature

        with open(self.name, 'r') as f: #apro il file in modalità lettura

            next(f)

            for line in f:
                line = line.strip() #elimino spazi e \n
                line = line.replace('-', ',')   #rimpiazzo i - con le , per avere l'anno separato dal mese
                line = line.split(',')    #divido le righe usando le , come separatore
                try:
                    line[2] = float(line[2])
                    line[1] = int(line[1])
                    line[0] = int(line[0])
                except ValueError:
                    print("Value not valid\n")
                    continue    #se il valore non è valido il processo continua, senza aggiungere la riga alla lista
                temperatures.append(line)   #aggiungo la riga alla lista

        return temperatures



def compute_variations (time_series, first_year, last_year, N):

    variations = {} #dizionario finale con le variazioni ogni N anni

    all_years = {}  #dizionario con le liste dei valori annuali

    current_year = first_year    #il primo anno in fila

    data_year = []  #lista di valori del singolo anno

    for line in time_series:

        if line[0] >= first_year and line[0] <= last_year+1 and current_year == line[0]: #finchè l'anno rimane lo stesso aggiungo i valori alla lista
            data_year.append(line[1])

        elif line[0] >= first_year and line[0] <= last_year+1:   #quando si cambia anno
            all_years[current_year] = data_year    #aggiungo la lista al dizionario
            current_year = line[0]  #cambio l'anno da confrontare
            data_year = [line[0]]  #resetto la lista, inserendo il primo nuovo valore

    print(all_years)

    means = {}

    for year in all_years.keys():   #calcolo tutte le medie per ogni singolo anno
        means[year] = sum(all_years[year])/len(all_years[year]) #somma dei valori diviso il numero dei valori

    if N > len(all_years.items()): raise ExamException("The value of the window is not valid\n")    #se N ha una valore maggiore del numero di anni, viene alzato un errore

    c = 0
    
    for year in all_years.keys():   #mi scorre tutti gli anni richiesti

        sum_m = 0
        print(year)
        if c != N:    #somma le medie fino a che non sono N, a meno che non sia arrivato alla fine
            sum_m += means[year]
            c += 1

            if year == last_year:   #salvo la variazione con l'ultimo anno
                variations[year] = means[year] - sum_m/c

        else:   #arrivato a N e resetto il contatore
            variations[year] = means[year] - sum_m/c
            c = 0
            continue

    return variations



def control_temperature (time_series, min_T, max_T):

    all_years = {}  #dizionario con le liste dei valori annuali

    current_year = time_series[0][0]    #il primo anno in fila

    data_year = []  #lista di valori del singolo anno

    for line in time_series:

        if current_year == line[0]: #finchè l'anno rimane lo stesso aggiungo i valori alla lista
            data_year.append(line[2])

        else:   #quando si cambia anno
            all_years[current_year] = data_year    #aggiungo la lista al dizionario
            current_year = line[0]  #cambio l'anno da confrontare
            data_year = [line[0]]  #resetto la lista, inserendo il primo nuovo valore

    for year in all_years.keys():

        if min(all_years[year]) < min_T: print(f"In {year} there's a value lower than the min\n")

        if max(all_years[year]) > max_T: print(f"In {year} there's a value bigger than the max\n")


#test
time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()
variations = compute_variations(time_series, 1900, 1904, 3)
print(variations)
#control_temperature(time_series,30, 30)