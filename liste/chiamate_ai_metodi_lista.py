#1.1. Aggiunta singola in coda: append()
#
# Nota: il metodo append e' preferibile rispetto all'operatore +
#       in quanto append non deve generare un nuovo oggetto ogni
#       volta.

L = [1,2,3,4]

L.append(5)         # [1,2,3,4,5]

#1.2. Aggiunta multipla in coda: extend()

L.extend([6,7,8])   # [1,2,3,4,5,6,7,8]

#1.3. Aggiunta in posizione arbitraria: insert()
#
#   la insert non elimina, semplicemente aggiunte nella posizione scelta
#   spostando a destra l'elemento che si trova nella posizione scelta

L.insert(3, "4")    # [1,2,3,'4',4,5,6,7,8]

#2.1. Rimozione singola in coda: pop()

last = L.pop()      # [1,2,3,'4',4,5,6,7]

#2.2. Rimozione singola in posizione arbitraria: pop(i)

third = L.pop(3)    # [1,2,3,4,5,6,7]


#2.3. Rimozione singola in posizione arbitraria: del

del L[3]            # [1,2,3,5,6,7] rimozione singola

#2.4. Rimozione multipla in posizione aribitraria: del

del L[0:2]          # [3,5,6,7]     rimozione multipla

#2.5. Rimozione multipla in posizione arbitraria: sezionamento

L[1:3] = []         # [3,7]

#Nota:  L[1:] = [] e' diverso da L[1] = []

#  altri metodi: 
#
#   - L.reverse() | reversed()
#   - L.sort() | sorted()
#   - index()

#3. Inversione
#   3.1 L.reverse() modifica sul posto, non crea nuova lista
#   3.2 reversed()  crea nuova lista
L.reverse()

LL = list(reversed(L))

#4. Ordinamento
#   4.1 L.sort() utilizza il metodo di confronto standart di Python
#       quindi confronti tra stringhe ascendente. Per modificare il
#       comportamento dell'ordinamento con argomenti keyword key e reverse.
#
#       key e' una funziona che accetta un solo argomento e restituisce
#       il valore da utilizzare per l'ordinamento
#       reverse e' un booleano e stabilisce se l'ordinamento e' decrescente

L = ["abc", "ABD", "aBe"]

L.sort()    # ["ABD","aBe","abc"]

L.sort(key=str.lower)   # ["abc", "ABD", "aBe"] effettua una conversione 
                        # a minuscolo e poi ordina

L.sort(key=str.lower, reverse=True) # ["aBe","ABD","abc"] conversione e 
                                    # ordinamento inverso



# Nota importante:  sia append() che sort() modificano la lista sul post
#                   senza ritornare nulla (None). Quindi fare questo:
#                   L = L.append(4) ci fa perdere il riferimento ala lista
#                   L e' None adesso.

#   4.2 sorted()

sorted(L, key=str.lower, reverse=True) # ["aBe", "ABD", "abc"]

# Nota: possiamo convertire in minuscolo tramite mappatura di lista
#       prima di effettuare l'ordinamento, ma in questo caso il 
#       risultato contiene i valori trasformati

sorted([x.lower() for x in L], reverse=True)    # ["abe", "abd", "abc"]


# Nota 2.6 vs 3.0:  in sort() python2.6 i confronti tra tipi di oggetti diversi
#                   es:str e list, funzionano e vengono effettuati tramite 
#                   regole prefissate. Le regole di ordinamento sono basate sui
#                   nomi dei tipi: es: "int" < "str"
#
#                   in sort() python3.0 tutto questo e' cambiato, il confronto
#                   tra oggetti di tipi eterogenei genera un errore invece che
#                   effettuare un ordinamento con regole prefissate.
#                   es: [1,2,'tre'].sort() ERRORE
#
#                   Python2.6 permetteva il passaggio di una funzione arbitraria#                   per effettuare l'ordinamento con sort().
#                   Python3.0 non permette piu' cio'. L'unica possibilita' e'
#                   utilizzare l'argomento keyword key=funzione dove funzione
#                   effettua trasformazioni di valori durante l'ordinamento.
#
#                   Python2.6 permette entrambe le tecniche.


#5. Indice elemento
#
#   5.1 index() ritorna l'indice di un elemento

pos = L.index("ABD") #pos = 1




