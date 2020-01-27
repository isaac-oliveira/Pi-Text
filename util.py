def removeSpaceAndBreakLine(item):
    return item != '\n' and item != ' '

def filterData(data):
    aux = []
    for line in data:
        for elem in line:
            if(removeSpaceAndBreakLine(elem)):
                aux += [int(elem)]
    return aux