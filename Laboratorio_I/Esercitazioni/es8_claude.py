class ExamException(Exception):
    pass

class PhoneBookFile:
    def __init__(self, name):
        self.name = name
    
    def get_contacts(self): #restituisce la lista dei contatti divisa in dizionari
        contacts = []
        try:
            with open(self.name, 'r') as f:
                c = 0
                next(f) #salto l'header
                for line in f:
                    dic = {}
                    line = line.strip()
                    line = line.split(',')
                    print(line)
                    if not len(line) == 4: continue #controlla che la lista sia composta da i 4 elementi richiesti
                    dic["nome"] = line[0]
                    dic["cognome"] = line[1]
                    dic["telefono"] = line[2]
                    if line[3] == '': dic["email"] = None   #l'email può essere omessa
                    else: dic["email"] = line[3]
                    contacts.append(dic)
                    c+=1
                if c <=1: raise ExamException("There aren't such informations\n")
        except FileNotFoundError:
            raise ExamException('ERROR: File not found\n')
        return contacts
    
class PhoneBook:
    def __init__(self, contacts):
        self.contacts = contacts

    def search(self, query):    #cerca per nome o per cognome
        searched = []
        if not isinstance(query, str): raise ExamException('The type is incorrect\n')
        if query == '': raise ExamException('The string is empty\n')
        for contact in self.contacts:
            if query == contact["nome"] or query == contact["cognome"]:
                searched.append(contact)
        return searched

    def get_duplicates(self):   #cerca contatti con lo stesso numero di telefono
        duplicates = []
        for contact_i in self.contacts:
            for contact_j in self.contacts:
                if contact_i["telefono"] == contact_j["telefono"]:
                    duplicates.append(contact_i)
        return duplicates
    
    def export_sorted(self, field): #ordina la lista per il campo richiesto
        sorted_contacts = []
        if not isinstance(field, str): raise ExamException("It's not a string\n")
        field = field.lower()   #rendo tutto minuscolo per avere case-insensitive
        if field == "nome":
            sorted_contacts = sorted(self.contacts, key = lambda d: d["nome"])
        elif field == "cognome":
            sorted_contacts = sorted(self.contacts, key = lambda d: d["cognome"])
        elif field == "telefono":
            sorted_contacts = sorted(self.contacts, key = lambda d: d["telefono"])
        else: ExamException("Not valid value\n")
        return sorted_contacts

pb_file = PhoneBookFile(name='rubrica.csv')
contacts = pb_file.get_contacts()
pb = PhoneBook(contacts)
results = pb.search("ros")
print(results)
# [{"nome": "Mario", "cognome": "Rossi", ...}, ...]
dups = pb.get_duplicates()
print(dups)
# [{"telefono": "333111222", "contatti": ["Mario Rossi", "Anna Rossi"]}, ...]
sorted_list = pb.export_sorted("cognome")
print(sorted_list)
# lista ordinata alfabeticamente per cognome