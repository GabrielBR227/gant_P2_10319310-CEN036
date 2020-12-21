#!/usr/bin/env python3

#importando biblioteca sys
import sys

#convertendo o argumento pego na tecla do usuário para letras maiúsculas
gene = sys.argv[1].upper()

#colocando o códon de início 
begin =  'ATG'

#achando a posição do último nucleotídeo do códon de início e o primeiro do códon de parada
inicio = gene.index(begin)+ 2
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
	
print(inicio, '\n' , parada)
