# concatenazione

T = (1,2) + (3,4)
print T

# ripetizone

T = (1,2) * 2		# stampa (1,2,1,2)
print T

# indicizzazione e sezionamento

T = (1,2,3,4)
TT = T[0], T[1:3]	#stampa (1, (2,3))

# virgole e parentesi
#
# in python le parentesi possono racchiudere anche le espressioni
# per indicare una tupla con un singolo oggotto bisogna usare la
# notazione (x,) con la virgola finale.

x = (40)	#assegna l'intero 40 alla variabile x

y = (40,)	#una tupla contente un intero (40,)

# Nota: python permette di omettere le parentesi di apertura e di chiusura
#	l'unico caso in cui le parantesi per le tuple sono obbligatorie e'
#	quando la tupla e' passata come parametro ad una funzione
