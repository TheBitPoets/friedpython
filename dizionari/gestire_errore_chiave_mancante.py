
D = {"uno": 1, "due":2 , "tre": 3}

#1. in

if "cinque" in D
    print D["cinque"]
else
    print("error")


#2. try/except

try:
    print D["cinque"]
except KeyError:
    print("error")

#3. metodo get

print D.get("cinque", "error")
