"""
ESERCIZIO 3: Stampa tutte le chiavi del dizionario creato nell'esercizio1 usando il metodo keys()
successivamente stampa tutti i valori con il metodo values(). Scegliere se usare il for oppure
mettere chiavi e valori in una lista e stampare la lista
"""

eng2it = {}

eng2it['one'] = 'uno'
eng2it['two'] = 'due'
eng2it['three'] = 'tre'
eng2it['four'] = 'quattro'
eng2it['five'] = 'cinque'

for k in eng2it.keys():
    print(k)

print()

for v in eng2it.values():
    print(v)

print()

K = list(eng2it.keys())
V = list(eng2it.values())

print(K)
print(V)