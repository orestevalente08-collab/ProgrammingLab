class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, window):
        if not isinstance(window, int) or window <= 0:
            raise ExamException('Il valore da inserire deve essere di tipo intero\n')
        self.window = window
    
    def compute(self, lista):
        if not isinstance(lista, list): raise ExamException('Deve essere inserita una lista\n')
        if(lista == []): raise ExamException('Errore, lista valori vuota\n')
        for item in lista:
            try:
                if not isinstance(item, float): raise ExamException('I valori nella lista devono essere numeri\n')
            except ValueError:
                raise ExamException('I valori nella lista devono essere numeri\n')
        if(len(lista)<self.window): raise ExamException("La lunghezza della finestra non può essere maggiore di quella della lista\n")
        media_m = []
        for i in range(0, len(lista)):
            sum = 0
            for idx in range(i, i+self.window, 1):
                sum = sum + lista[idx]
            media_m.append(sum/self.window)
        return media_m

lista = [2, 4, 8, 16]
media_mobile = MovingAverage (2)
media = media_mobile.compute(lista)
print(media)