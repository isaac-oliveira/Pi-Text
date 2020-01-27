import os

def read(path):
    aux = []
    with open(path, 'r') as file:
        aux += [x for x in file]
        file.close()
    return aux

def write(data, filename):
    if not os.path.exists('Resultados'):
        os.makedirs('Resultados')
    with open('Resultados/' + filename, 'w+') as file:
        for lines in data:
            file.write(lines + '\n')
        file.close()
