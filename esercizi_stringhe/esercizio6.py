"""
Esercizio 6 – Stringa al contrario (while)
Scrivi un programma Python che stampi una stringa al contrario utilizzando un ciclo while, una
variabile di ciclo i e la funzione len().
"""

s = 'banana'
invertita = ''
i = 0
while i < len(s):
    invertita += s[len(s)-1-i]
    i += 1

print(invertita)

invertita2 = ''
for indice in range(len(s)-1,-1,-1):
    invertita2 += s[indice]
print(invertita2)