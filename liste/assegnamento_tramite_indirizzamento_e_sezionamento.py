#   Entrambi indirizzamento e sezionamento sono modifiche
#   sul posto, quindi l'oggetto viene modificato direttamente
#   piuttosto che generare una nuova lista come risultato

#1. assegnamento per indirizzamento

L = ["uno","due","tre","quattro"]

L[0] = "1" # ["1", "due", "tre", "quattro"]

#2. assegnamento per sezionamento
#
#   pensare al sezionamento diviso in due passi
#   a. cancellazione elementi indicata a sinistra di =
#   b. aggiunta elementi indicata a destra di =
#

L[1:3] = ["2", "3"] # sostituisco "due" e "tre"
                    # ["1", "2", "3", "quattro"]

#   il numero di elementi inseriti non deve essere
#   uguale a quelli cancellati
#
#   in questo modo i sezionamenti possono essere usati
#   per: 1.sostituire 2.estendere 3.cancellare

L[2:3] = [] #elimino il terzo elemento ["1", "2", "quattro"]
L[1:]  = [] #elimino tutto tranne il primo elemento ["1"]

L[0:1] = ["tante", "stringhe", "al posto", "di 1"]
