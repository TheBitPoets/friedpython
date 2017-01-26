# scrivere un file di testo
#
# write: scrive i testo su di un file
#        al contrario di print write non agggiunge \n
#        che devono essere aggiunti esplicitamente nel testo
#
# Nota: in python3.0 write ritorna il numero di byte scritti
#       non in python2.6

myfile = open("myfile.txt", "w")	#apro un file in scrittura
myfile.write("hello world\n")		#scrivo del testo
myfile.close()				#chiudo il file

# leggere un file di testo 
#
# read: leggo il contenuto di un file di testo tutto in una volta

myfile = open("myfile.txt", "r")
data = myfile.read()	#leggo tutto il file
print(data)

# leggo un file di testo riga per riga
#
# l'oggeto di tipo file ritorna ad ogni iterazione
# una nuova riga
#
# questo modo di leggere un file e' preferibile alla read
# garantisce un uso ottimale della memoria e viene eseguita
# piu' volocemente

for line in open("myfile"): #modo accesso r e' default
	print(line, end='')


