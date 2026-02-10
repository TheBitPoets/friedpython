"""
ESERCIZIO 1: Ciclo While e Indici
Scrivi un programma che stampi tutti gli elementi della lista utilizzando un ciclo while e la
funzione len(). Gestisci manualmente l'indice per scorrere la lista.
"""

numeri = [12, 45, 7, 23, 64, 10, 33, 24, 88, 5] 

i = 0
while i < len(numeri):
    print(numeri[i])
    i += 1