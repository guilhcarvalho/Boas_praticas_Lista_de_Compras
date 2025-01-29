"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
#Importação modulo cmd
import os
import time

#Criação da lista de compras
compras = []

#Loop while == True
while True:
    #Opções de entrada
    print('LISTA DE COMPRAS.')
    print('Selecione uma opção.')
    entradas = input(f'[A]Adicionar, [D]eletar, [L]Listar Items, [S]Sair -->   ').lower()

    #Executando escolha do usuario.
    if entradas == 'a':
        os.system('cls')
        adicionar = input(f'Adicione um produto a lista:  ')
        if adicionar not in compras:
            compras.append(adicionar)
            print('Produto adicionado.')
            time.sleep(2)
            os.system('cls')
        else:
            print('Esse produto já está na lista.')
            time.sleep(2)
            os.system('cls')
            
    elif entradas == 'd':
        os.system('cls')
        excluir = input(f'Digite qual produto gostaria de excluir:  ').lower()

        if excluir not in compras:
            print('Produto não encontrado.')
            print('Voltando a tela inicial')
            time.sleep(2)
            os.system('cls')
            
        else:    
            compras.remove(excluir)
            print('Produto excluido.')
            time.sleep(2)
            os.system('cls')
            
    elif entradas == 'l':
        os.system('cls')
        if len(compras) == 0:
            print('Lista de compras vazia.')
            
        else:
            for i in enumerate(compras):
                indice, produto = i
                print(f'{indice} {produto.capitalize()}')
        limpar = input(f'Voltar a seleção inicial? [S]   ').lower()
        if limpar == 's':
            os.system('cls')
    
    elif entradas == 's':
        break
    
    else:
        print(f'Escolha uma das alternativas.')
