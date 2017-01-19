import json
#creare un dizionario
D = {"spam": 2, "ham": 1, "eggs": 3}

#l'ordine di inserimento non e' l'ordine di visualizzazione

#numero di elementi
l = len(D)

#test di appartenza di una chiave
"ham" in D

#creo una lista dalle chiavi

# keys() 
# python2 ritorna la lista delle chiavi
# python3 ritorna un iteratore, e' necessario
#         chiamare list
list(D.keys())
