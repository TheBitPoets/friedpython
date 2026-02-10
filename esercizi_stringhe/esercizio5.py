"""
Esercizio 5 – Conteggio caratteri
Scrivi un programma Python che conti e stampi il numero totale di caratteri presenti nella stringa.
"""

# con ciclo while
s = 'banana'
i = 0
conta = 0 # variabile per contare il numero di caratteri
while i <len(s):
    if s[i] == 'a':
        conta += 1
    i += 1
print(conta)


# con ciclo for
conta = 0
for carattere in s:
    if carattere == 'a':
        conta += 1
print(conta)
