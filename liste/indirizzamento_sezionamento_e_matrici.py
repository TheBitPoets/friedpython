#   indizzamento e sezionamento non eliminano, restituiscono sempre
#   il primo  una copia dell'elemento alla posizione selezionata
#   il secondo una nuova lista

#1. Indirizzamento

L = [0,1,2,3,4]

e = L[2] #seleziono il terzo elemento (2), gli indici partono da zero

e = L[-2] #seleziono il secondo elemento da destra (3)

#2. Sezionamento
#
#   il sezionamento estrae sottoparti

L = ["a", "b", "c", "d"]

LL = L[1:3] #seleziono b e c partenza:fine(escluso)


#3. Matrici a due dimensioni
#
#   uno dei metodi pre rappresentare matrici e' l'uso
#   di liste annidate

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

e = matrix[2][1] #seleziono 7

