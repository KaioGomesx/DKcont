# -*- coding: utf-8 -*-
from art import *
option = ficha = 0

print('×'*50)
tprint('D4RK')
print('''\033[1;32m[*]Criador: D4RK SYST3M
[*]Canal Do Youtube: https://www.youtube.com/channel/UCUKyY5rDaAGKdNKAd8XXbwQ 

[*]Grupo Do Telegran: https://t.me/joinchat/KpcuPFRwrDINubprpTATAA

[*]Finalidade: Resolver calculos e problemas matematicos

[*]Versão: 1.0 Criada em 18/09/2019
\033[m''')
print('×'*50)
print('▬'*15,'\033[1;34m MATEMATICA\033[m','▬'*12)
print( '<'*8,'\033[1;32mESCOLHA UMA QUANTIDADE DE FICHAS\033[m', '>'*7)
ficha = int(input('Digite quantas fichas voce quer: '))
print( '<'*13,'\033[1;32mESCOLHA UMA OPÇÃO\033[m', '>'*13)

for x in range(1,ficha +1):
	print('''
	\033[1;32m[1]MATEMATICA\033[m
	\033[1;33m[2]FISICA\033[m
	\033[1;36m[3]FAZER PESQUISA NO WIKIPEDIA
	\033[1;34m[4]PARA CONTINUAR\033[m
	\033[1;35m[5]REGRAS E INFORMACOES DO JOGO
	\033[1;31m[6]PARA SAIR\033[m''')
	option = int(input('\033[1;33mDigite a Opção Desejada: \033[m'))
	if option == 1:
		import m1
	if option == 2:
		import m2
	if option == 3:
		import m5
	if option == 5:
		import m4
	if option == 6:
		break
		
	
	
		
		


































