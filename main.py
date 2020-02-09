from pbm import Pbm
from mask import Mask
from manipulator import Manipulator
from text import Text
# Exemplo: Imagens/grupo_07_imagem_1_linhas_30_colunas_2_palavras_277.pbm
path = input('Digite o caminho do arquivo: ')
pbm = Pbm(path)
mask = Mask('Mascaras/mask-dilation.txt')
manipulator = Manipulator(pbm)
manipulator.applyMedian()
manipulator.applyDilation(mask)
text = Text(pbm)
text.showInfo()
# O nome sem a extensão Ex: grupo_07_imagem_1_linhas_30_colunas_2_palavras_277
name = input('Digite o nome do arquivo: ')
pbm.save(name)