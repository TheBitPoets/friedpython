# i gestori di contesto permettono di inserire il processamento
# dei file in una logica in grado di garantire che essi vengano
# chiusi automaticamente quando necessario invece di affidarsi
# alla chiusura automatica scatenato dal rilascio della memoria

with open("myfile.txt") as myfile
	for line in myfile:
		print line

# try/finally fornisce funzionalità simili ma richiede più codice
# da scrivere

myfile = open("myfile.txt")
try:
	for line in myfile:
		print line
finally:
	myfile.close()
