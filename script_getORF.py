#!/usr/bin/env python3

#importando biblioteca sys
import sys

#convertendo o argumento pego na tecla do usuário para letras maiúsculas
gene = sys.argv[1].upper()

#colocando o códon de início
begin =  'ATG'

#achando a posição do último nucleotídeo do códon de início
if begin in gene:
	inicio = gene.index(begin)+ 2
else:
	print('**********Não há códon de início************')	
	sys.exit()

#achando a posição do primeiro nucleotídeo do códon de parada

parada1 = gene.index('TAA')
parada2 = gene.index('TAG')
parada3 = gene.index('TGA')

if parada1 > inicio:
	parada = parada1
elif parada2 > inicio:
	parada = parada2
elif parada3 > inicio:
	parada = parada3
else:
	print('Não há códon de parada')
	sys.exit()


print(gene[inicio:parada])
