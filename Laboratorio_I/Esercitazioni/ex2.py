class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):

        self.name = name

    
    def get_data(self):

        data = []   #lista di liste finale

        with open(self.name, 'r') as f: #apro il file nella variabile f

            for line in f:
                line = line.strip() #tolgo spazi e \n nella riga
                data.append(line.split(','))    #separo sfruttando le ,

        return data
    


def compute_variations(time_series, first_year, last_year):

    variations = {}
    years = {}
    current_year = first_year
    length = 0
    sum_values = 0

    for idx, line in enumerate(time_series):

        line[0] = line[0].split('-')    #separo anno e mese

        try:    #provo a convertire l'anno in un intero e la media in un float
            line[0][0] = int(line[0][0])
            line[1] = float(line[1])
        except ValueError: continue

        if line[0][0]>= first_year and line[0][0] <= last_year+1: #controllo che l'anno considerato si trovi nel range

            if line[0][0] == current_year:
                sum_values += line[1]
                length += 1

            else:
                try:    #controllo che ci siano i valori
                    years[current_year] = sum_values/length
                except ZeroDivisionError: continue
                
                length = 1  #resetto tutto
                sum_values = line[1]
                current_year = line[0][0]


    current_year = first_year  #anno precedente
    for year in years.keys():

        if year == first_year: continue    #se siamo al primo ciclo non fa niente

        variations[f"{current_year}-{year}"] = years[year] - years[current_year]    #calcola le variazioni
        current_year = year

    return variations







time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(compute_variations(time_series, 1951, 1955))