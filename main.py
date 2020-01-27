from pbm import Pbm
from mask import Mask
from manipulator import Manipulator

path = input('Digite o caminho do arquivo: ')
pbm = Pbm(path)
path = input('Digite o caminho da mascara: ')
mask = Mask(path)
manipulator = Manipulator(pbm)
manipulator.applyMedian(mask)
name = input('Digite o nome do arquivo: ')
pbm.save(name)