class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        with open(self.name, 'r') as f:
            lines = []
            f = f.readlines()[1:]
            for line in f:
                line = line.replace("-", ",")
                lines.append(line.split(","))
            return lines

def compute_variations(time_series, first_year, last_year):
    for line in time_series:
        line[2] = line[2].strip()
        if not line[2].isdigit():
            print("Errore: valore non numerico")
            line[2] = 0
        line[2] = float(line[2])
        if not line[0].isdigit():
            print("Errore: valore non numerico")
            line[0] = 0
        line[0] = int(line[0])
    print(time_series)
    somme = []
    for idx, line in enumerate(time_series):
        sum = 0
        for i in range(idx, idx+12):
            sum = sum + line[2]
        somme.append(sum)
    try:
        dic = {line[0] : (somme[idx]/12) - (somme[idx-1]/12) for idx, line in enumerate(time_series) if (line[0] >= first_year and line[0] <= last_year) }
    except TypeError:
        print(line[0])
    return dic

time_series_file = CSVTimeSeriesFile('data.csv')
time_series_file = time_series_file.get_data()
print(compute_variations(time_series_file, 1952, 1960))
