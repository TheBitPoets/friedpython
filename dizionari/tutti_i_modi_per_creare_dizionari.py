#1. letterale tradizionale
#Nota:  questa forma e' utile
#       se si conosce a priori
#       il contenuto del dizonario
D = {"uno": 1, "due": 2, "tre": 3}

#2. assegnazione dinamica di chiavi

D = {}

D["uno"] = 1
D["due"] = 2
D["tre"] = 3

#3. chiamata a dict con argomenti keyword
#Nota:       richiede che le chiavi siano
#            tutte stringhe

dict(uno=1, due=2, tre=3)

#4. chiamata dic con lista di tuple (chiave,valore)

lista_di_tuple = [("uno",1), ("due",2), ("tre",3)]
dict(lista_di_tuple)
dict([("uno",1),("due",2),("tre",3)])

#5. variante del metodo 4. con metodo zip
#Nota:      zip costruisce tuple da liste

L1 = ["uno", "due", "tre"]
L2 = [1,2,3]

list(zip(L1,L2))

#quindi nel nostro caso
#si usa zip per raccogliere in tuple chiavi e valori

dict(zip(["uno","due","tre"],[1,2,3]))

#6. Solo nel caso in cui tutte le chiavi devono avere lo
#   stesso valore, si usa il metodo fromkeys

dict.fromkeys(["uno","due","tre"],0)

#7. Solo in python3 i dizionari possono essere creati con
#   espressioni di mappatura

D = {k:v for (k,v) in zip(["uno","due","tre"],[1,2,3])}

D = {k:0 for k in ["uno","due","tre"]} #equivalente fromkeys()

