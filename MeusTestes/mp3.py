import pygame
from os import system
pygame.init()

#Função para tocar a música

def mp3(musica) :
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    pygame.event.wait()
    enter = input('Pressione enter para continuar')

#Função para lmpar a tela

def cls() :
    system('cls')

#Perguntar qual estilo de música a pessoa quer :

cls()
while True:

    print(f'''{'=' * 50}
Selecione o tipo de música que quer escutar: 
{'=' * 50}
[1] ROCK
[2] POP
[3] TRAP
[4] Sair do programa
{'=' * 50}''')
    opcao = int(input('Sua opção:'))

#Opção do ROCK

    if opcao == 1 :

        cls()

        print(f'''{'=' * 50}
Selecione a música que quer escutar: 
{'=' * 50}
[1] Pais e Filhos - Legião Urbana
[2] Wish You Were Here - Pink Floyd
[3] Smells Like Teen Spirit - Nirvana 
{'=' * 50}''')

        opcaoMusic = int(input('Sua opção: '))

        if opcaoMusic == 1 :
            mp3('ROCK/Pais_e _Filhos.mp3')

        elif opcaoMusic == 2 :
            mp3('ROCK/Wish You Were Here - Pink Floyd.mp3')

        elif opcaoMusic == 3 :
            mp3('ROCK/Smells Like Teen Spirit - Nirvana.mp3')

#Opção do POP

    elif opcao == 2:

        cls()

        print(f'''{'=' * 50}
Selecione a música que quer escutar: 
{'=' * 50}
[1] Águas de Março - Elis Regina
[2] Alegria, Alegria - Caetano Veloso
[3] Amei Te Ver - Tiago Iorc
{'=' * 50}''')

        opcaoMusic = int(input('Sua opção: '))

        if opcaoMusic == 1:
            mp3('POP/Águas de Março - Elis Regina.mp3')

        elif opcaoMusic == 2 :
            mp3('POP/Alegria, Alegria - Caetano Veloso.mp3')

        elif opcaoMusic == 3 :
            mp3('POP/Amei Te Ver - Tiago Iorc.mp3')

#Opção do TRAP

    elif opcao == 3:

        cls()

        print(f'''{'=' * 50}
Selecione a música que quer escutar: 
{'=' * 50}
[1] Dollar - Only
[2] Peita da Lacoste - Mystic! - Tema
[3] Nike 12 Molas - Yamashita
{'=' * 50}''')

        opcaoMusic = int(input('Sua opção: '))

        if opcaoMusic == 1:
            mp3('TRAP/Dollar - Only.mp3')

        elif opcaoMusic == 2 :
            mp3('TRAP/Peita da Lacoste - Mystic! - Tema.mp3')

        elif opcaoMusic == 3 :
            mp3('TRAP/Nike 12 Molas - Yamashita.mp3')

#Opção para sair do programa

    if opcao == 4 :
        break
