"""
1. Scrivi una funzione conta_vocali(testo).
"""

def cerca_vocali(testo):
    contatore = 0
    vocali = ['a', 'e', 'i', 'o', 'u']
    for carattere in testo:
        if carattere in vocali:
            contatore += 1
    return contatore

s = 'ciao mamma'
print(s)
print(cerca_vocali(s))

"""
2. Scrivi una funzione palindroma(testo) che verifica se una stringa è palindroma.
"""

def palindroma(testo):
        testo = "".join(testo.split(" "))
        x = int(len(testo) / 2)
        for i in range(0, x):
             if testo[i] == testo[len(testo)-1-i]:
                  continue
             else:
                  return False
        return True

frasi = ['i nasi sani', 'io vado da voi', 'ciao mamma', 'È corta e atroce']
for frase in frasi:
     print(palindroma(frase), frase)


"""
3. Scrivi una funzione inverti_parole(frase).
"""

def inverti_parole(frase):
     parole = frase.split(" ")
     invertite = []
     for parola in parole:
          invertite.append(
               "".join(
                    reversed(parola)
               )
          )
     return " ".join(invertite)

s = "ciao mamma guarda come mi diverto"
print(s)
print(inverti_parole(s))

"""
4. Scrivi una funzione lunghezza_media_parole(frase).
"""

def lunghezza_media_parole(frase):
     somma = 0
     parole = frase.split(" ")
     for parola in parole:
          somma += len(parola)
     return somma / len(parole)

print(s)
print(lunghezza_media_parole(s))
     

"""
5. Scrivi una funzione sostituisci_spazi(testo) con underscore.
"""

def sostituisci_spazi(testo):
     return "_".join(testo.split(" "))

print(sostituisci_spazi(s))

"""
6. Scrivi una funzione trova_parola_piu_lunga(frase).
"""

def trova_parola_piu_lunga(frase):
     parola_max = None
     lunghezza = 0
     for parola in frase.split(" "):
          if len(parola) > lunghezza:
               parola_max = parola
               lunghezza = len(parola)
     return parola_max

print(trova_parola_piu_lunga(s))

"""
7. Scrivi una funzione conta_maiuscole(testo).
"""

def conta_maiuscole(testo):
     contaore = 0
     for carattere in testo:
          if carattere.isupper():
               contaore += 1
     return contaore

s = 'CiAo MaMmA'
print(s)
print(conta_maiuscole(s))

def conta_maiuscole2(testo):
     contatore = 0
     for carattere in testo:
          if ord(carattere) >= 65  and ord(carattere) <= 90:
               contatore += 1
     return contatore

print(conta_maiuscole2(s))

"""
8. Scrivi una funzione rimuovi_punteggiatura(testo).
"""

def rimuovi_punteggiatura(testo):
     filtrato = ""
     for carattere in testo:
          if (ord(carattere) >= 65 and ord(carattere) <= 90 ) or (ord(carattere) >= 97 and ord(carattere) <= 122):
               filtrato += carattere
     return filtrato

s = "?;:-_@{}ciao mamma^$%ABC....!"
print(s)
print(rimuovi_punteggiatura(s))

"""
9. Scrivi una funzione iniziali_nome(nome_completo).
"""

def iniziali_nome(nome_completo):
     nome, cognome = nome_completo.split(" ")
     return nome[0], cognome[0]

nome_completo = "Antonio Caristia"
print(nome_completo)
print(iniziali_nome(nome_completo))

"""
10. Scrivi una funzione comprimi_stringa(testo) (es: aaabb → a3b2).
"""

def comprimi_stringa(testo):
     s = ""
     contatore = 1
     for i in range(0, len(testo)):
          if i < len(testo)-1 and testo[i+1] == testo[i]:
               contatore += 1
          else:
               s += testo[i]
               if contatore > 1: s += str(contatore)
               contatore = 1
               print(s)
     return s

s = 'aaabbcdd'
print(s)
print(comprimi_stringa(s))
