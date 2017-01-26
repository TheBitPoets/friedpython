# ordinamento tupla
# le tuple non sono mutabile, quindi per ordinare una tupla
# e' necessario prima trasformala in lista, ordinarla, ricreare
# una nuova tupla
#
# Nota: in questo esempio list e tuple vengono utilizzate per convertire
#       una tupla in una lista e viceversa, entrambe le chiamate creano
#       nuovi oggetti

T = (3,1,4,2,9,0)
tmp = list(T)
tmp.sort()
T = tuple(tmp)

# stessa operazione con sorted()
# sorted restituisce una lista

T = (3,1,4,2,9,0)
T = tuple(sorted(T))

# creare liste da tuple con espressioni di mappatura
#
# Nota: le espressioni di mappatura ritornano sempre liste, ma possono
#	iterare su una qualsiasi sequenza (tuple, stringhe e altre liste)

T = (1,2,3,4,5)

L = [x + 20 for x in T]		# L = [21,22,23,24,25]

# In generale le tuple non hanno gli stessi metodi delle liste e delle stringhe
# in quanto immutabile. Pero' index e count funzionano lo stesso.

T = (1,2,3,2,4,2)

i = T.index(2)	#l'indice del primo 2

ii = T.index(2,2) #l'indice del primo 2 dopo il terzo elemento

n = T.count(2)	#quanti due ci sono 

# Nota:	l'immutabilta' delle tuple vale solo per gli elementi del primo livello
#	non per gli oggetti annidati (lista dentro tupla)

T = (1, [2,3], 4)
T[1] = 0 #errore
T[1][0] = 'ciao' # ok mutabile (1, ['ciao',3], 4)

