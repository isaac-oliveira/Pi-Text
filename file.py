def read(path):
    aux = []
    with open(path, 'r') as file:
        aux += [x for x in file]
        file.close()
    return aux

def write(data, filename):
    with open(filename, 'w+') as file:
        for lines in data:
            file.write(lines + '\n')
        file.close()
