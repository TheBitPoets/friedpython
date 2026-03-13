"""
1. Scrivi una funzione media_lista(lista) che restituisca la media dei numeri contenuti in una lista.
"""

def media_lista(L):
    """
    versione con ciclo for
    """
    somma = 0
    for elem in L:
        somma += elem
    media = somma / len(L)
    return media

def media_lista_while(L):
    """
    versione con ciclo while
    """
    i = 0
    somma = 0
    while(i<len(L)):
        somma += L[i]
        i += 1
    media = somma / len(L)
    return media

L = [10, 6, 7, 23, 34, 55, -2, 16, 3]

print(media_lista(L))
print(media_lista_while(L))

"""
Scrivi una funzione filtra_pari(lista) che restituisca una nuova lista contenente solo i numeri pari.
"""
def filtra_pari(L):
    LL = [] # lista dei numeri pari di L
    for elem in L:
        if elem % 2 == 0:
            LL.append(elem)
    return LL

def filtra_pari_while(L):
    i = 0
    LL = []
    while i<len(L):
        if L[i] % 2 == 0:
            LL.append(L[i])
        i += 1
    return LL

print(filtra_pari(L))
print(filtra_pari_while(L))

"""
3. Scrivi una funzione massimo_differenza(lista) che restituisca la differenza tra il massimo e il minimo.
"""

def massimo_differenza(L):
    max = L[0]
    min = L[0]
    for elem in L:
        if elem > max:
            max = elem
        if elem < min:
            min = elem
    print(f"max = {max} min = {min}")
    return max - min

def massimo_differenza_while(L):
    max = L[0]
    min = L[0]
    i = 0
    while(i<len(L)):
        if L[i] > max:
            max = L[i]
        if L[i] < min:
            min = L[i]
        i += 1
    print(f"max = {max} min = {min}")
    return max - min

print(massimo_differenza(L))
print(massimo_differenza_while(L))

"""
4. Scrivi una funzione inverti_lista(lista) senza usare reverse().
"""

def inverti_lista(L):
    LL = [] # lista con i valori inverti
    for indice in range(len(L)-1, -1, -1):
        LL.append(L[indice])
    return LL

def inverti_lista_while(L):
    i = len(L)-1
    LL = []
    while(i >= 0):
        LL.append(L[i])
        i -= 1
    return LL

print(L)
print(inverti_lista(L))
print(inverti_lista_while(L))

"""
5. Scrivi una funzione conta_maggiori(lista, soglia) che conta quanti numeri sono maggiori di soglia.
"""

def conta_maggiore(L, s):
    contatore = 0
    for elem in L:
        if elem > s:
            contatore += 1
    return contatore

def conta_maggiore_while(L, s):
    contatore = 0
    i = 0
    while(i < len(L)):
        if L[i] > s:
            contatore += 1
        i += 1
    return contatore

print(conta_maggiore(L, 11))
print(conta_maggiore_while(L, 11))

"""
6. Scrivi una funzione somma_indici_pari(lista) che somma gli elementi agli indici pari.
"""

def somma_indici_pari(L):
    somma = 0
    for index, elem in enumerate(L):
        if index % 2 == 0:
            somma += elem
    return somma

def somma_indici_pari_range(L):
    somma = 0
    # il terzo argomento di range è il  passo
    # genera la sequenza di numeri pari
    # 0 2 4 6 ..
    for indice in range(0, len(L), 2):
        somma += L[indice]
    return somma

def somma_indici_pari_while(L):
    i = 0
    somma = 0
    while i < len(L):
        somma += L[i]
        i += 2
    return somma

print(somma_indici_pari(L))
print(somma_indici_pari_range(L))
print(somma_indici_pari_while(L))


"""
7. Scrivi una funzione rimuovi_duplicati(lista) che restituisce una lista senza duplicati.
"""

def rimuovi_duplicati(L):
    LL = []
    for elem in L:
        if elem not in LL:
            LL.append(elem)
    return LL

def rimuovi_duplicati_while(L):
    LL = []
    i = 0
    while i < len(L):
        if L[i] not in LL:
            LL.append(L[i])
        i += 1
    return LL

print(rimuovi_duplicati(L+L))
print(rimuovi_duplicati_while(L+L))

"""
8. Scrivi una funzione unisci_liste(l1, l2) che restituisce una nuova lista alternando gli elementi.
"""

def unisci_liste(L1, L2):
    L3 = [] # lista unione
    for indice in range(0, max(len(L1), len(L2))):
        print(indice)
        if indice >= len(L1): pass
        else: L3.append(L1[indice])
        if indice >= len(L2): pass
        else: L3.append(L2[indice])
    return L3

print(unisci_liste(L, [0,0,0,0,0]))

"""
9. Scrivi una funzione prodotto_lista(lista) che moltiplica tutti gli elementi.
"""

def prodotto_lista(L):
    prodotto = 1
    for elem in L:
        prodotto *= elem
    return prodotto

def prodotto_lista_while(L):
    prodotto = 1
    i = 0
    while i < len(L):
        prodotto *= L[i]
        i += 1
    return prodotto

print(prodotto_lista(L))
print(prodotto_lista_while(L))

"""
10. Scrivi una funzione trova_secondo_massimo(lista).
"""

def trova_secondo_massimo(L):
    primo_massimo = L[0]
    secondo_massimo = 0
    for elem in L:
        if elem > primo_massimo:
            secondo_massimo = primo_massimo
            primo_massimo = elem
    return secondo_massimo

def trova_secondo_massimo_while(L):
    primo_massimo = L[0]
    secondo_massimo = 0
    i = 0
    while i < len(L):
        if L[i] > primo_massimo:
            secondo_massimo = primo_massimo
            primo_massimo = L[i]
        i += 1
    return secondo_massimo

print(trova_secondo_massimo(L))
print(trova_secondo_massimo_while(L))