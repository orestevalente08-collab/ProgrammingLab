class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):

        try:    #provo ad aprire il file per vedere se esiste

            f = open(name, 'r')

        except FileNotFoundError: raise ExamException("File not Found\n")   #alza un errore se non trova il file
        except FileExistsError: raise ExamException("File doesn't exist\n") #alza un errore se il file non esiste

        f.close()

        self.name = name




    def get_data(self, country):

        data = []   #inizializzo una lista vuota

        with open(self.name, 'r') as f:

            next(f)    #salto header

            for line in f:
                line = line.strip() #tolgo gli spazi e i \n
                line = line.split(',')    #divide le righe usando come separatore la ,

                if line == ['']: continue #controlla che la riga non sia vuota

                if line[2] == country:  #aggiungo la liste in base alla nazione richiesta

                    try:    #controllo che non ci siano problemi di conversione
                        data.append([line[0], float(line[1])])
                    except ValueError:
                        continue
        
        if data == []: raise ExamException("The country doesn't exists\n")  #se la lista è vuota vuol dire che non ha trovato il paese richiesto

        return data
    


def compute_variations(time_series_1, time_series_2, first_year, last_year):

    variations = {}

    year_1 = {}

    for line in time_series_1:  #prendo i valori del primo time series che si trovano nel range

        line[0] = line[0].split('-')

        try:
            line[0][0] = int(line[0][0])

        except ValueError: continue
    
        if line[0][0] >= first_year and line[0][0] <= last_year+1:

            if line[1] != "":
                year_1[line[0][0]] = line[1]


    
    year_2 = {}

    for line in time_series_2:  #prendo i valori del time series che si trovano nel range

        line[0] = line[0].split('-')


        try:
            line[0][0] = int(line[0][0])

        except ValueError: continue
    
        if line[0][0] >= first_year and line[0][0] <= last_year+1:

            print(line[0])

            if line[1] != "":
                year_2[line[0][0]] = line[1]

    print(year_1)
    print(year_2)

    for idx in range(first_year, last_year+2):

        variations[idx] = sum(year_1.values())/len(year_1.values()) - sum(year_2.values())/len(year_2.values()) #calcolo della differenza delle medie

    return variations









time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByCountry.csv")
time_series_italy = time_series_file.get_data(country="Italy")
time_series_kuwait = time_series_file.get_data(country="Kuwait")
variation = compute_variations(time_series_italy, time_series_kuwait, 1900, 1902)
print(variation)
