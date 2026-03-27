class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
    
    def saluta(self):
        print('Ciao sono', self.ruolo + ",", self.nome, self.cognome)

class Studente(Persona):
    def __init__(self, nome, cognome, corso):
        super().__init__("Studente UNITS", nome, cognome)
        if corso is None:
            self.corso = []
        else:
            self.corso = corso

    def add_corso(self, corso):
        self.corso.append(corso)
    
    def saluta(self):
        Persona.saluta(self)
        print("> Frequento il corso: ", self.corso)
    
    def active_courses(self, list_doc = None):
        if list_doc is None:
            list_doc = []
        else:
            list_doc = list_doc
        
        for doc in list_doc:
            if doc.common_courses(self):
                print("C'è un insegnante che insegna tutti i corsi")
            else:
                print("Non c'è un insegnante che insegna tutti i corsi")

class Docente(Persona):
    def __init__(self, nome, cognome, corso):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso = corso

    def add_corso(self, corso):
        self.corso.append(corso)

    def common_courses(self, studente):
                sorted(self.corso)
                sorted(studente.corso)
                check = True
                for i in self.corso:
                    for j in studente.corso:
                        if self.corso != studente.corso:
                            check = False
                            break
                return check
    
    def saluta(self):
        Persona.saluta(self)
        print("> Docente del corso: ", self.corso)

corsi = ["Analisi", "Laboratorio", "Programmazione", "Geometria"]
obj_Irene = Studente("Irene", "Rossi", corsi)
obj_Irene.saluta()
obj_DelSanto = Docente("Daniele", "Del Santo", corsi)
obj_Nenzi = Docente("Laura", "Nenzi", "Programmazione")

if obj_Irene.common_courses(obj_DelSanto):
    print("Hanno gli stessi corsi\n")
else:
    print("Non hanno gli stessi corsi\n")

obj_Irene.active_courses([obj_DelSanto, obj_Nenzi])