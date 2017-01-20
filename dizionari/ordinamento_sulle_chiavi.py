#1. in python 2.6 si utilizzavav il metodo sort() di list
#   dopo chiamata a keys()

D = {1: "uno", 2: "due", 3: "tre"}

keys = D.keys()
sorted_keys = keys.sort()

for k in sorted_keys:
    print D[k]

#   in python 3.0 keys() restituisce una vista
#   bisogna usare list e poi sort in questo modo

keys = list(D.keys())
sorted_keys = keys.sort()

for k in sorted_keys:
    print D[k]

#   in python 3.0 si può anche usare sorted che accetta
#   un iterabile

for k in sorted(D):
    print D[k]
