# open apre un file. 
# open accetta tre parametri (il terzo e' opzionale):
# - il nome del file
#   puo' contenere un percorso (assoluto o relativo)
#   se non viene specificato un percorso si assume che
#   il file risieda nella dir corrente (dove lo script
#   viene eseguito)
#
# - il modo di accesso
#   r lettura, w scrittura, a accodamento, b binario
#
# - controllo del buffer
#   se 0 i dati vengono trasferiti direttamente 
#   durante le operazioni di scrittura

#file aperto in scrittura
output = open(r"./esempio.txt", "w")

#file aperto in lettura
input = open(r"./esempio.txt". "r")

#file aperto in lettura scrittura
input_output = open(r"", "r+")
