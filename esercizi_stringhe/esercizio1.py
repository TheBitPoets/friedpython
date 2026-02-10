"""
Esercizio 1 – Ciclo while
Scrivi un programma Python che, data una stringa, stampi tutti i suoi caratteri uno per riga
utilizzando un ciclo while, una variabile di ciclo i e la funzione len().
"""

s = 'banana'
i = 0
while i < len(s):
    print(s[i])
    i += 1 # i = i + 1