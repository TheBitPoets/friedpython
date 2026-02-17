"""
ESERCIZIO5: Data la stringa s = 'supercalifragilistichespiralidoso'
Creare un dizionario che contenga come chiavi tutti i caratteri che compaiono in s
e come valori il numero delle occorrenze del carattere in s. Al termine stampa il
dizionario che hai ottenuto. Dovresti ottenere qualcosa di simile.
{'s': 4, 'u': 1, 'p': 2, 'e': 2, 'r': 3, 'c': 2, 'a': 3, 'l': 3, 'i': 6, 'f': 1, 'g': 1, 't': 1, 'h': 1, 'd': 1, 'o': 2}
"""

D = {}
s = 'supercalifragilistichespiralidoso'

for c in s:
    if c not in D:
        D[c] = 1
    else:
        D[c] += 1

print(D) 

D = {}

for c in s:
    D[c] = D.get(c, 0) + 1

print(D)