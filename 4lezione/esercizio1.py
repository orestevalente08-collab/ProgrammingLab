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
    
    def common_courses(self, Docente):
        for cd in self.corso:
            for cs in Docente.corso:
                if cd == cs:
                    return False
        return True
    
    def active_courses(self, list_doc = None):
        if list_doc is None:
            list_doc = []
        else:
            list_doc = list_doc
        
        for doc in list_doc:
            if self.common_courses(doc):
                print("C'è un insegnante che insegna tutti i corsi")
            else:
                print("Non c'è un insegnante che insegna tutti i corsi")

class Docente(Persona):
    def __init__(self, nome, cognome, corso):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso = corso

    def add_corso(self, corso):
        self.corso.append(corso)

    def saluta(self):
        Persona.saluta(self)
        print("> Docente del corso: ", self.corso)

corsi = ["Analisi", "Laboratorio", "Programmazione", "Geometria"]
obj_Irene = Studente("Irene", "Rossi", corsi)
obj_Irene.saluta()
obj_DelSanto = Docente("Daniele", "Del Santo", "Analisi")

if obj_Irene.common_courses(obj_DelSanto):
    print("Hanno gli stessi corsi\n")
else:
    print("Non hanno gli stessi corsi\n")

obj_Irene.active_courses([obj_DelSanto])