class ExamException(Exception):
    pass

class GradeFile:
    def __init__(self, name):
        self.name = name

    def get_grades(self):   #crea una lista di dizionari con tutte le info
        grades = []
        try:
            with open(self.name, 'r') as f:
                next(f) #salta l'header
                c = 0
                for line in f:
                    dic = {}
                    line = line.strip()
                    line = line.split(',')
                    try:
                        dic["matricola"] = int(line[0])
                    except ValueError:
                        print("The matricola is not numeric\n")
                        continue
                    dic["nome"] = line[1]
                    try:
                        if (int(line[2])>= 18 and int(line[2])<= 30):
                            dic["voto"] = int(line[2])
                            c += 1
                        else:
                            dic["voto"] = ""
                    except ValueError:
                        if line[2] == "30L":    #trasformo il 30L in 31 in modo che sia più facile confrontarlo con gli altri voti
                            dic["voto"] = 31
                            c += 1
                        else:
                            print("Not valid valutation\n")
                            dic["voto"] = ""
                    grades.append(dic)
                if c<=1: raise ExamException("There are not enough informations\n")
                for idx, line_i in enumerate(grades):
                    succ_grades = grades[idx+1:]
                    for line_j in succ_grades:
                        if line_i["matricola"] == line_j["matricola"]:
                            print("There's a duplicated matricola\n")
        except FileNotFoundError:
            raise ExamException("ERROR: File not found\n")
        return grades

def compute_statistics(grades): #ritorna un dizionario con tutte le statistiche globali
    dic = {}
    if grades == []: raise ExamException("The list is empty\n")
    voti = [d["voto"] for d in grades if d["voto"] != ""]
    dic["min"] = min(voti) #calcola il minimo
    dic["max"] = max(voti) #calcola il massimo
    if dic["max"] == 31: dic["max"] = "30L" #se il massimo corrisponde a 31 allora quello è un 30L
    dic["media"] = sum(voti)/len(voti)   #calcola la media
    if len(voti)%2 != 0:  #calcola la mediana
        dic["mediana"] = voti[len(voti)//2]
    else:
        dic["mediana"] = (voti[len(voti)//2]+voti[(len(voti)//2)+1])//2
    dic["bocciati"] = 0
    dic["promossi"] = 0
    for line in grades: #calcola i promossi e i bocciati
        if line["voto"] == "": dic["bocciati"] += 1
        else: dic["promossi"] +=1
    return dic

def compute_grade_distribution(grades): #calcola il numero di voti in base alla distribuzione
    distribution = {}
    distribution["18-21"] = 0
    distribution["22-25"]  =  0
    distribution["26-28"] = 0
    distribution["29-30"] = 0
    distribution["30L"] = 0
    for line in grades:
        if not isinstance(line["voto"], str):
            if line["voto"]>=18 and line["voto"]<= 21: distribution["18-21"] += 1
            elif line["voto"]>=22 and line["voto"]<= 25: distribution["22-25"] += 1
            elif line["voto"]>= 26 and line["voto"]<= 28: distribution["26-28"] += 1
            elif line["voto"]>= 29 and line["voto"]<= 30: distribution["29-30"] += 1
            elif line["voto"] == 31: distribution["30L"] += 1
    return distribution

gf = GradeFile(name='voti.txt')
grades = gf.get_grades()
print(grades)
stats = compute_statistics(grades)
print(stats)
# {"media": 25.3, "mediana": 26.0, "min": 18, "max": 30,
# "promossi": 42, "bocciati": 5}
dist = compute_grade_distribution(grades)
print(dist)
# {"18-21": 8, "22-25": 12, "26-28": 14, "29-30": 6, "30L": 2}