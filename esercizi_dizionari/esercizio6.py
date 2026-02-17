"""
ESERCIZIO6: Data la stringa s = 'supercalifragilistichespiralidoso'
ricreare il dizionario dell'esercizio 5 e chiamarlo D. A partire da
D creare un secondo dizionario DD che abbia come chiavi i valori di
D e come valori le chiavi di D 
"""

s = 'supercalifragilistichespiralidoso'
D = {}

for c in s:
    D[c] = D.get(c, 0) + 1

print(D)

DD = {}

for k in D:
    if D[k] not in DD:
        DD[D[k]] = [k]
    else:
        DD[D[k]].append(k)

print(DD)