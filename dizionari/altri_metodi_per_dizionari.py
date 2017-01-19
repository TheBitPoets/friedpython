D = {"spam": 2, "ham": 1, "eggs": 3}

#lista di valori

D.values()

list(D.values())

#tuple (chiave, valore)

D.items()

list(D.items())

#recuperare un elemento

D["spam"]

#recuperare una chiave che non esiste genera un errore (KeyError)
#il metodo get() restituisce in questo caso un valore di default (None)

D.get("spam")       #ritorna None in caso di KeyError
D.get("spam", 0)    #ritorna 0 in caso di KeyError

#unire due dizionari (concatenazione)

D2 = {"toast": 4, "muffin": 5}

#il metodo update fonde le chievi e i valori di due dizionari
#sovrascrivendo senza alcuna segnalazione le chiavi duplicate
D.update(D2)

#eliminazione e prelevamento di un elemento

del D["spam"]

#il metodo get elimina una chiave dal dizonario e restituiscve
#il corrispondente valore eliminato. E' simile al modot pop delle
#liste solo che accetta una chiave non un indice.
value = D.pop("spam")
