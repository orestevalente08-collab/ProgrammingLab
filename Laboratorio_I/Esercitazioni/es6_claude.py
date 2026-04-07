from datetime import datetime #libreria per gestire le date

class ExamException(Exception):
    pass

class CSVDailySeriesFile:   #classe per gestire file .csv
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        lines = []
        try:
            with open(self.name, 'r') as f: #apro il file in read mode in una variabile f
                next(f) #salta l'header
                counter = 0
                for idx_i, line_i in enumerate(f):  #valuto ogni riga del file aperto
                    line_i = line_i.strip()
                    lines.append(line_i.split(','))
                    if line_i == '':
                        raise ExamException("There's a empty line\n")
                
                for idx_i in range(len(lines)):
                    for idx_j in range(idx_i+1, len(lines)):  #controlla elemento per elemento
                        if lines[idx_i] == lines[idx_j]:    #controlla se ci sono duplicati
                            raise ExamException('There are some duplicates\n')
                
                for i, line in enumerate(lines):    #valuto la nuova lista che ho creato riga per riga
                    for idx,item in enumerate(line):
                        try:
                            line[idx] = datetime.strptime(item, '%Y-%m-%d')
                            counter+=1
                        except ValueError:
                            try:
                                line[idx] = float(item)
                                counter+=1
                            except ValueError:  # se non lo riesco a convertire nei due tipi richiesti, prosegui
                                print('Type of value incorrect\n')
                                continue
                print(lines)

                if counter<2:   #se il file non ha almeno due righe blocca tutto
                    raise ExamException("The file don't have such data\n")
                return lines
        except FileNotFoundError:   #se non trovo il file, blocca tutto
            raise ExamException("File not found\n")
    
class TimeSeriesResampler:
    def __init__(self, data):
        self.data = data
    
    def interpolate(self):  #restituisce la lista iniziale completa dei valori mancanti
        completed_data = []
        for idx, line in enumerate(self.data):
            if line[1] == '' and idx != 0 and idx != -1:    #completa la lista interpolando i valori(non considera il primo e l'ultimo elemento)
                line[1] = round((self.data[idx-1][1] + self.data[idx+1][1])/2, 2)   #arrotonda le cifre a 2 decimali
            completed_data.append(line)
        return completed_data
    
    def resample(self, frequency):  #calcola la media mensile o settimanale
        if frequency != "monthly" and frequency != "weekly":    #controllo che l'input sia giusto
            raise ExamException("Invalid value\n")
        
        if frequency == "monthly":  #calcola la media mensile
            months = {}
            current_month = self.data[0][0].month
            sum =  0
            length = 0
            for date, value in self.data:
                try:
                    if(date.month==current_month):    #somma finchè il mese non cambia
                        sum += value
                        length += 1
                        continue
                except AttributeError:
                    print("C'è una data non valida\n")
                    continue
                months[f'{date.year}-{date.month}'] = sum/length
                current_month = date.month
                sum = 0
                length = 0
            return months
            
        elif frequency == "weekly": #calcola la media settimanale
            weeks = {}
            for idx, line in enumerate(self.data):
                sum = 0
                for i in range(idx, idx+7): #calcola la somma ogni 7 giorni
                    sum += line[1]
                weeks[f'week {idx+1}'] = sum/7
            return weeks
    
f = CSVDailySeriesFile(name='daily.csv')
data = f.get_data()
resampler = TimeSeriesResampler(data)
filled = resampler.interpolate()
weekly = resampler.resample("weekly")
# {"2024-W01": 112.4, "2024-W02": 118.7, ...}
monthly = resampler.resample("monthly")
# {"2024-01": 115.2, "2024-02": 121.0, ...}
print(weekly)
print(monthly)