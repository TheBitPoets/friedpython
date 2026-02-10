"""
ESERCIZIO 6: Conta occorrenze di tutti i caratteri in una parola
Scrivi un frammento di codice che crei una lista dove gli indici sono il valore ascii dei carattere
e usa questa lista per tenere traccia delle occorrenze dei carattere in una parola.
Usa la funzione ord() per ottenere il valore ascii di un carattere e la funzione chr() per l'operazione
inversa.
"""

L = []
i = 0
while i < 256:
    L.append(0)
    i += 1

print(L, end=' ')

s = 'Supercalifragilistichespiralidoso'

i = 0
while i < len(s):
    L[ord(s[i])] += 1
    i += 1

for index, elem in enumerate(L):
    print(chr(index), elem)