"""
ESERCIZIO 3: Ricerca del Massimo
Scrivi un algoritmo che individui il numero più grande presente nella lista senza utilizzare la
funzione predefinita max(). Stampa il risultato finale.
"""

numeri = [12, 45, 7, 23, 64, 10, 33, 24, 88, 5]

max = numeri[0]
i = 0
while i < len(numeri):
    if numeri[i] > max:
        max = numeri[i]
    i += 1

print(max)

max = numeri[0]
for num in numeri:
    if num > max:
        max = num
print(max)