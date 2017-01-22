#1. Creare una lista

L = [1,2,3,4,5]

#2. Lunghezza della lista: len()

n_elem = len(L)

#3. Concatenazione

# L'operatore + effettua la concatenazione tra liste

L = L + [6,7] #ok

# + si aspetta lo stesso tipo di sequenza su ambo i lati
# altrimenti viene generato un errore

L = L + "6" + "7" #errore, L e' sequenza lista, "6" e "7" sequenza stringa

L = L + list("6") #oppure L = str(L) + "6"

#4. Ripetizione

L = ["ciao"]

L = L * 4 #["ciao","ciao","ciao","ciao"]
