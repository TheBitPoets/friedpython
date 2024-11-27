# le stringhe sono sequenze immutabili
#
# sequenze: hanno un ordine posizionale da sx a dx
#           altri tipi di sequenze sono liste o tuple
#
# immutabili: non possono essere modificate sul posto
#
# le stinghe supportano operazioni sulle espressioni
# (concatenamento, sezionamento) o sui metodi stringa

# Nota: in python3 esistono due tipi di stringhe str e byte
#       str: utilizzato per testi unicode (ascii e non)
#       byte: utilizzato per dati binari
#       bytearray: variante mutabile di byte
#
#       in python 2.6 esistono str e unicode
#       str: usato per dati ascii che binari
#       unicode: usato per testo unicode

# Letterali stringa
#
# apici singoli 'testo'
# apici doppi   "testo"
# apici tripli  """testo"""
# stringhe raw  r"testo"

print("uso i doppi se inserisco nella stringa ' ")
print('uso i singoli se inserisco nella stringa "" ')

# concatenazione implicita

print("questo " "e' del " 'testo' " concatenato")

# sequenze di escape: permettono di inserire nel testo
#                     caratteri non stampabili

print("tabulazione \t a capo \n e tanti altri")

print("per stampare una backslash raddoppio in questo modo \\ ")

print("se python non riconosce la sequenza di escape la ignora, \p non esiste ")

# stringhe raw: non vengono interpretate le squenze di escape

path = "C:\new\text.dat" #interpreta \n come sequenza di escape
path = r"C:\new\text.dat"#stringa raw, \n non viene interpretato come sequenza escape

# Nota: per indicare i percorsi dei file sia sotto unix che windows
#       e' possibile utilizzare | al posto di \ o /

# Nota: una stringa raw non può terminare con un numero dispari di \

# apici tripli


print("""
    con gli apici tripli
    costrusco la stringa quando la scrivo
    senza preoccuparmi di inserire sequenza di escape
    per tabulazione o a capo
""")
