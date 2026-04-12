#Oreste Valente SM32A00011

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):

        self.name = name


    
    def get_data(self, city):

        temperatures = []

        try:    #provo ad aprire il file
            with open(self.name, 'r') as f: #apro il file come f

                for line in f:

                    line = line.strip() #tolgo spazi e \n
                    line = line.split(',')  #separo i valori

                    try:    #prova a trasformare l'anno in un intero dopo averlo separato
                        line[0] = line[0].split('-')
                        line[0][0] = int(line[0][0])
                    except ValueError: continue

                    if line[2] == city: #controlla che la città sia corretta
                        try:
                            temperatures.append([line[0], float(line[1])]) #aggiunge i valori solo se possono essere di tipo float
                        except ValueError: continue

                if temperatures == []: raise ExamException("City not found\n")
        
        except FileNotFoundError: raise ExamException("File not Found\n")

        return temperatures



def compute_slope(time_series, first_year, last_year):  #calcola il momento angolare

    months = 0  #variabile per controllare se i mesi validi sono 12
    years = {}  #variabile che unisce l'anno ai suoi valori
    values = [] #variabile con medie annuali
    current_year = first_year   #per controllare quando l'anno cambia

    for line in time_series:

        if line[0][0] >= first_year and line[0][0] <= last_year:  #controlla che l'anno si trovi nel range richiesto

            if current_year == line[0][0]:  #controllo che l'anno non sia cambiato
                values.append(line[1])
                months += 1
                if months == 12 and line[0][0] == last_year:    #controlla anche l'ultimo anno
                    years[current_year] = values


            elif current_year != line[0][0]:
                if months == 12:    #controllo che tutti e 12 i mesi abbiamo valori validi
                    years[current_year] = values
                values = [line[1]] #resetto tutto
                months = 1
                current_year = line[0][0]

    if years == {}: raise ExamException("Invalid range\n")

    print(years)

    
    means = {}

    for year in years.keys():

        means[year] = sum(years[year])/len(years[year]) #calcola le medie per anno

    print(means)

    n = len(means.keys())
    if n == 0: raise ExamException("There are no means\n")
    year_mean = sum(means.keys())/n #calcola la media degli anni
    values_mean = sum(means.values())/n   #calcola la media dei valori delle medie annuali


    num = 0
    den = 0

    for year, value in means.items():

        num += (year - year_mean) * (value - values_mean) #calcolo il numeratore
        den += (year - year_mean)**2 #calcolo il denominatore
    
    try:
        m = num/den #calcolo il momento angolare
    except ZeroDivisionError: raise ExamException("The denominator is equal to zero\n")

    return m







time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByMajorCity.csv")
time_series_italy = time_series_file.get_data(city="Rome")
print(time_series_italy)
slopes = compute_slope(time_series_italy, 1950, 2001)
print(slopes)

