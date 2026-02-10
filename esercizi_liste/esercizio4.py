"""
ESERCIZIO 4: Conteggio Condizionale
Scrivi un programma che conti quanti numeri pari sono contenuti nella lista. Stampa alla fine
il conteggio totale (es: "I numeri pari sono: 4").
"""

numeri = [12, 45, 7, 23, 64, 10, 33, 24, 88, 5] 

conta_pari = 0
for num in numeri:
    if num % 2 == 0:
        conta_pari += 1
print("I numeri pari sono: ", conta_pari)
