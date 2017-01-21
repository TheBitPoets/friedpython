L = [1,2,3,4,5]

#1. len()

n_elem = len(L)

#2. concatenazione

#L'operatore + effettua la concatenazione tra lista
#si aspetta lo stesso tipo di sequenza su ambo i lati
#altrimenti viene generato un errore

L = L + [6,7] #ok

L = L + "6" + "7" #errore, L e' sequenza lista, "6" e "7" sequenza stringa

L = L + list("6") #oppure L = str(L) + "6"

#3. Ripetizione

L = ["ciao"]

L = L * 4 #["ciao","ciao","ciao","ciao"]
