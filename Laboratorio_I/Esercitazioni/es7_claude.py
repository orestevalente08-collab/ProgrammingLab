from datetime import datetime

class ExamException(Exception):
    pass

class LogFile:
    def __init__(self, name):
        self.name = name

    def get_events(self):
        dic = {}
        try:
            with open(self.name, 'r') as f:
                
                for line in f:  #divido il file in un dizionario in base al tipo di evento
                    line = line.strip()
                    line = line.split(' | ')
                    try:
                        line[0] = datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        print("Type of a line is incorrect\n")
                        continue
                    dic[line[2].upper()] = [line[0], line[1]]

        except FileNotFoundError:
            raise ExamException("File not found\n")
        return dic

class LogAnalyzer:
    def __init__(self, ls):
        self.ls = ls
    
    def filter_by_level(self, level):   #restituisce solo gli eventi del livello indicato
        level_events = {}
        if not isinstance(level, str):
            raise ExamException('The input type is incorrect\n')
        
        level = level.strip()   #tolgo eventuali spazi dalla stringa inserita
        level = level.upper()   #rendo la parola tutta maiuscola per renderlo case-insensitive

        for line in self.ls.items():
            print(line)
            if line[1][1] == level:
                level_events[line[0]] = line[1]

        if level_events == []:
            print(f'Not found any levels called {level}\n')
        return level_events
    
    def compute_hourly_distribution(self): #restituisce dizionario con conteggio di eventi per ora del giorno
        counters = {}
        c = 0
        if self.ls == []:
            raise ExamException('The list is empty\n')
        
        current_hour = next(iter(self.ls.values()))
        current_hour = current_hour[0].hour
        for line in self.ls.values():
            if(line[0].hour == current_hour):
                c += 1
            else:
                current_hour = line[0].hour
                counters[line[0]] = c
                c = 0
        return counters
    
    def find_bursts(self, window_minutes, threshold):   #individua le finestre temporali con almeno tot eventi
        windows = []
        c = 0
        current_minute = next(iter(self.ls.values()))
        current_minute = current_minute[0].minute

        for idx, line in enumerate(self.ls.values()):
            if idx % window_minutes == 0:
                if c >= threshold:
                    windows.append([f"{current_minute} - {line[0].minute}", c])
                    current_minute = line[0].minute
                    c = 0
                else:
                    c = 0
            else:
                c += 1
        return windows


log = LogFile(name='app.log')
events = log.get_events()
# [{"timestamp": "2024-03-01 14:32:07",
# "level": "ERROR", "message": "connessione persa"}, ...]
analyzer = LogAnalyzer(events)
errors = analyzer.filter_by_level("ERROR")
dist = analyzer.compute_hourly_distribution()
# {0: 3, 1: 0, ..., 23: 12}
bursts = analyzer.find_bursts(window_minutes=5, threshold=10)
print(bursts)
# [{"start": "2024-03-01 14:30:00",
# "end": "2024-03-01 14:35:00", "count": 13}, ...]