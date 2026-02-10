"""
ESERCIZIO 5: Inversione della Lista
Scrivi un frammento di codice che crei una nuova lista contenente gli stessi elementi della
lista originale ma in ordine inverso (dall'ultimo al primo).
"""

numeri = [12, 45, 7, 23, 64, 10, 33, 24, 88, 5] 

inversa = []

for elem in reversed(numeri):
    inversa.append(elem)

print(inversa)
