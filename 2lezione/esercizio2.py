def is_palindromo (stringa):
    for i, l in enumerate(stringa):
        if(l != stringa[-i-1]):
            return False
    return True

s = input("Inserisci una frase: ")
is_palindromo(s)