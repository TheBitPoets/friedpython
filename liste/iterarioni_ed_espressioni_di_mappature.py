#1. Appartenza: in

3 in [1,2,3,4] #True|False

#2. Iterazione lista: for

for x in [1,2,3,4]:
    print(x, end=' ')

#3. Itarazione lista: mapputura di lista
#
#   mappatura di lista: meccanimo per crare nuove liste
#   applicando una espressione ad ogni elemento di una
#   sequenza: lista, stringa, tupla

res = [c*4 for c in "ciao"] # ["cccc", "iiii", "aaaa", "oooo"]

#lo stesso risultato con ciclo for

res = []
for c in "ciao":
    res.append(c*4)


#4. Funzione map()
#
#   la funzione map() applica una funzione a ogni elemento
#   di una sequenza restituendo una nuova lista

res = map(abs, [-1,-2,-3])

#con ciclo for

res = []
for x in [-1,-2-3]:
    res.append(asb(x)) 
