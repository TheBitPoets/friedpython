# Sia in python2.6 che python3.0 e' possibile aprire un file binario
# usando il modo d'accesso b nella chiamata open
#
# Nota: in python3.0 file di testo e binari sono gestiti separatamente
#       - file di testo - sono gestiti tramite oggetti str, effettuano
#	automaticamente la codifica/decodifica Unicode e convertono i
# 	caratteri di fine riga
#
#	- file binari - sono gestiti tramite oggetti bytes che non modificano
#	cio' che viene letto o scritto
#
# Nota: in python2.6 i file di testo gestiscono sia stringhe testuali ASCII
#	che a 8 bit, che dati binari. Il testo unicode viene gestito a parte
#	tramite le stringhe di tipo unicode

# apro un file binario in lettura

data = open("myfile.bin", 'rb').read()


