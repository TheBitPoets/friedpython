D = {"uno": 1, "due": 2, "tre": 3}

# 2.6

for key in D:
    print D[key]

for key in D.keys():
    print D[key]


# 3.0

for key in D:
    print D[key]

for key in list(D.keys()):
    print D[key]


