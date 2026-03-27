phrase = "the cat sat on the mat the cat"
parole = phrase.split(" ")
dic = {word: parole.count(word) for word in parole} #.count() fa sapere quante volte ha cicliato
print(dic)