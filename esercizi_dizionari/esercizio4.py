"""
ESERCIZIO4: date le seguenti strutture dati:

K = [1, 3, 7, 9]
V = ['uno', 'tre', 'sette', 'nove']
D = {1: 'uno', 2: 'due', 4: 'quattro', 5: 'cinque', 6: 'sei', 8: 'otto', 9: 'nove'}

Ciclare la lista K e contrallare se gli elementi in K sono presenti come chiavi in D, in caso
negativo inserire l'elemento come chiave in D e prendere come valore l'elemento in V nella
medesima posizione.

Al termine stampa D, dovresti ottnere qualcosa di simile
{1: 'uno', 2: 'due', 4: 'quattro', 5: 'cinque', 6: 'sei', 8: 'otto', 9: 'nove', 3: 'tre', 7: 'sette'}
"""

K = [1, 3, 7, 9]
V = ['uno', 'tre', 'sette', 'nove']
D = {1: 'uno', 2: 'due', 4: 'quattro', 5: 'cinque', 6: 'sei', 8: 'otto', 9: 'nove'}

for i,k in enumerate(K):
    if k not in D:
        D[k] = V[i]

print(D)