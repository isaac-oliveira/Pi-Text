def removeSpaceAndBreakLine(item):
    return item != '\n' and item != ' '

def filterData(data):
    aux = []
    for line in data:
        for elem in line:
            if(removeSpaceAndBreakLine(elem)):
                aux += [int(elem)]
    return aux

def calculateLineOrColumn(vetor):
    space = True
    num = 0
    for elem in vetor:
        aux = sum(elem)
        if(space and aux != 0):
            num = num + 1
            space = False
        elif (not space and aux == 0):
            space = True
    return num