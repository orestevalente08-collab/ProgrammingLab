from es2 import CSVTimeSeriesFile



class ExamException(Exception): #solleva degli errori

    pass



class SequenceFinder:

    def __init__(self, data):

        if (not isinstance(data, list)) or data == []:

            raise ExamException('The datas are not of the right type\n')
        
        if len(data) < 2:

            raise ExamException("There are not enough info\n")

        self.data = data



    def find_longest_streak(self, direction):

        if direction == "up":

            tmp = {}

            cresc = 0

            save = 0

            for idx, line in enumerate(self.data):

                current_line = self.data[idx-1]

                if line[2] > current_line[2]:  #conta la lunghezza della streak

                    cresc += 1

                else:

                    tmp[cresc] = save    #salvo in un dizionario temporaneo, tutte le lunghezze della streak e gli indici da cui iniziano

                    cresc = 0

                    save = idx

            max_streak = max(tmp.keys())   #prendo il massimo tra le lunghezze degli streak

            if max_streak < 2: raise ExamException("There are not enough element for a streak")

            streak = tmp[max_streak]    #prendo l'indice iniziale dello streak massimo

            values = []

            for idx in range(streak, max_streak + streak):

                values.append(self.data[idx][2])

            stats = {"start" : self.data[streak], "end" : self.data[max_streak + streak], "values" : values, "length" : max_streak}

            return stats   #ritorna la lista di tutti i valori appartenenti alla streak



        elif direction == "down":

            tmp = {}

            decr = 0

            save = 0

            for idx, line in enumerate(self.data):

                current_line = self.data[idx-1]

                if line[2] < current_line[2]:  #rimane nel ciclo fino a che non trova un valore minore del precedente

                    decr += 1

                else:

                    tmp[decr] = save    #salvo in un dizionario temporaneo, tutte le lunghezze della streak e gli indici da cui iniziano

                    decr = 0

                    save = idx
            
            min_streak = min(tmp.keys)   #prendo il massimo tra le lunghezze degli streak

            if min_streak < 2: raise ExamException("There are not enough element for a streak")

            streak = tmp[min_streak]    #prendo l'indice iniziale dello streak massimo

            values = []

            for idx in range(streak, min_streak + streak):

                values.append(self.data[idx][2])

            stats = {"start" : self.data[streak], "end" : self.data[min_streak + streak], "values" : values, "length" : min_streak}

            return stats   #ritorna la lista di tutti i valori appartenenti alla streak



        else:

            raise ExamException("The inserted value is invalid\n")



    def find_threshold_crossings(self, threshold):   #restituisce una lista di dizionari con i punti di crossing

        crossings = []

        if not isinstance(threshold, int or float): raise ExamException("The type is incorrect\n")

        for idx, line in enumerate(self.data):

            crossing = {}

            try:

                if int(line[2]) >= threshold and int(self.data[idx-1][2]) <= threshold: #up crossing points

                    crossing["direction"] = "up"

                    crossing["date"] = f"{line[0]}-{line[1]}"

                    crossing["value"] = line[2]

                    crossings.append(crossing)

                elif int(line[2]) <= threshold and int(self.data[idx-1][2]) >= threshold:   #down crossing points

                    crossing["direction"] = "down"

                    crossing["date"] = f"{line[0]}-{line[1]}"

                    crossing["value"] = line[2]

                    crossings.append(crossing)
            

            except ValueError:

                print("Not valid value\n")

                continue

        return crossings





tsf = CSVTimeSeriesFile(name='data.csv')

ts = tsf.get_data()

sf = SequenceFinder(ts)

streak = sf.find_longest_streak("up")
# {"start": "1949-06", "end": "1949-10",
# "length": 5, "values": [135, 148, 152, 160, 172]}

print(streak)

crossings = sf.find_threshold_crossings(200)
# [{"date": "1951-05", "direction": "up", "value": 204},
# {"date": "1952-01", "direction": "down", "value": 193}, ...]

print(crossings)