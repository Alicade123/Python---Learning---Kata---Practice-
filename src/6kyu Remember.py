def remember(str_):  
    results = []
    occ = {}
    for el in str_:
        if el in occ:
            results.append(el)
        else:
            occ[el] = 1
    return list(dict.fromkeys(results))

#Test Data
print(remember('apple'));  #["p"]
print(remember("limbojackassin the garden"));  #["a","s","i"," ","e","n"]
print(remember("11pinguin"));  #["1", "i", "n"]
print(remember("Claustrophobic"));  #["o"]
print(remember("apPle"));  #[]
print(remember("11 pinguin"));  #["1","i","n"]
print(remember('pippi'));  #["p","i"]
print(remember('Pippi'));  #["p","i"]
print(remember('kamehameha'));  #["a","m","e","h"]
print(remember(''));  #[]        