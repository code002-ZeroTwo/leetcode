def destCity(paths):
    sourcedest = []
    finaldest = []

    for path in paths:
        sourcedest.append(path[0])
        finaldest.append(path[1])

    print(sourcedest)
    print(finaldest)

    for city in finaldest:
        if city not in sourcedest:
            return city

    return ""
        
print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(destCity([["B","C"],["D","B"],["C","A"]]))