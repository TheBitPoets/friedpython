"""
1. Scrivi una funzione conta_lettere(testo) che restituisce un dizionario con la frequenza delle lettere.
"""

def conta_lettere(s):
    D = {}
    for carattere in s:
        if carattere not in D:
            D[carattere] = 1
        else:
            D[carattere] += 1
    return D

def conta_lettere2(s):
    D = {}
    for carattere in s:
        D[carattere] = D.get(carattere, 0) + 1
    return D

s = 'supercalifragilistichespiralidoso'
print(conta_lettere(s))
print(conta_lettere(s))

"""
2. Scrivi una funzione inverti_dizionario(d) che scambi chiavi e valori.
"""

def inverti_dizionario(D):
    DD = {}
    for chiave in D:
        if D[chiave] not in DD:
            DD[D[chiave]] = [chiave]
        else:
            DD[D[chiave]].append(chiave)
    return DD

def inverti_dizionario2(D):
    DD = {}
    for chiave in D:
        DD[D[chiave]] = DD.get(D[chiave], [])
        DD[D[chiave]].append(chiave)

    return DD

D = conta_lettere(s)
print(inverti_dizionario(D))
print(inverti_dizionario2(D))

"""
3. Scrivi una funzione studente_top(voti) che restituisca lo studente con il voto più alto.
"""

STUDENTI = {
    'Baggio': 10,
    'Totti': 3,
    'Del Piero': 6,
    'Balotelli': 2,
    'Chiesa': 8
}

def studente_top(STUDENTI):
    top = None
    voto = 0
    for studente in STUDENTI:
        if STUDENTI[studente] > voto:
            voto = STUDENTI[studente]
            top = studente
    return top, voto

studente_top, voto = studente_top(STUDENTI)
print(f"Lo studente top e' {studente_top} con voto {voto}")

"""
4. Scrivi una funzione somma_valori(d) che restituisca la somma dei valori numerici.
"""

def somma_valori(D):
    somma = 0
    for chiave in D:
        somma += D[chiave]
    return somma

print(len(s))
print(somma_valori(D))

"""
5. Scrivi una funzione filtra_valori(d, soglia) che restituisca solo le coppie con valore maggiore della soglia.
"""

def filtra_valori(d, soglia):
    filtrati = []
    for k in d:
        if d[k] > soglia:
            filtrati.append((k, d[k]))
    return filtrati

print(filtra_valori(STUDENTI, 6))

"""
6. Scrivi una funzione unisci_dizionari(d1, d2) sommando i valori delle chiavi comuni.
"""

NUMERI10 = {
    'Baggio': 10,
    'Totti': 10,
    'Del Piero': 10
}

def unisci_dizionari(d1, d2):
    d3 = {}
    for k in d1:
        if k in d2:
            d3[k] = d1[k] + d2[k]
            del d2[k]
        else:
            d3[k] = d1[k]
    
    for k in d2:
        d3[k] = d2[k]

    return d3

print(STUDENTI)
print(NUMERI10)
print(unisci_dizionari(STUDENTI, NUMERI10))

"""
7. Scrivi una funzione chiave_massima(d) che restituisca la chiave con il valore massimo.
"""

def chiave_massima(d):
    k_max, value_max = None, 0
    for k in d:
        if d[k] > value_max:
            k_max = k
            value_max = d[k]
    return k_max

print(STUDENTI)
print(chiave_massima(STUDENTI))

"""
8. Scrivi una funzione conta_parole(frase) che restituisca un dizionario parola->frequenza.
"""

def conta_parole(frase):
    D = {}
    parole = frase.split(" ")
    for parola in parole:
        if parola not in D:
            D[parola] = 1
        else:
            D[parola] += 1
    return D

s = "uno due tre uno uno quattro cinque due sette sette tre"

print(s)
print(conta_parole(s))

"""
9. Scrivi una funzione rimuovi_chiavi(d, lista_chiavi).
"""

def rimuovi_chiavi(d, lista_chiavi):
    for chiave in lista_chiavi:
        del d[chiave]

print(STUDENTI)
print('Balotelli', 'Totti')
rimuovi_chiavi(STUDENTI, ['Balotelli', 'Totti'])
print(STUDENTI)

"""
10. Scrivi una funzione media_valori(d).
"""

def media_valori(d):
    somma = 0
    for k in d:
        somma += d[k]
    return somma/len(d)

print(media_valori(STUDENTI))