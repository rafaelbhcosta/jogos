import random
import defs

rep = True

defs.linha()
print('Olá jogador, seja bem vindo ao jogo da velha')

while rep:
    computador = random.randint(1,3)
    defs.linha()
    escolha = int(input('Faça sua escolha\n1 - Pedra\n2 - Papel\n3 - Tesoura\nEscolha: '))
    
    if computador == escolha:
        defs.linha()
        print('Resultado do jogo')
        print(f'Computador: {computador}\nVocê: {escolha}\n\033[0;33mEMPATE\33[m')
    
    else:
        #Vitórias do jogador
        if escolha == 1 and computador == 3:
            defs.linha()
            escolha = 'Pedra'
            computador = 'Tesoura'
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\n\033[0;32mVocê venceu!!\33[m')

        elif escolha == 2 and computador == 1:
            defs.linha()
            escolha = 'Papel'
            computador = 'Pedra'
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\n\033[0;32mVocê venceu!!\33[m')

        elif escolha == 3 and computador == 2:
            defs.linha()
            escolha = 'Tesoura'
            computador = 'Papel'
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\n\033[0;31mVocê venceu!!\33[m')

        #Vitórias do computador
        elif computador == 1 and escolha == 3:
            defs.linha()
            escolha = 'Tesoura'
            computador = 'Pedra'
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\n\033[0;31mO cumputador venceu!!\33[m')

        elif computador == 2 and escolha == 1:
            defs.linha()
            escolha = 'Pedra'
            computador = 'Papel'
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\n\033[0;31mO cumputador venceu!!\33[m')

        elif computador == 3 and escolha == 2:
            defs.linha()
            escolha = 'Papel'
            computador = 'Tesoura'
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\n\033[0;31mO cumputador venceu!!\33[m')