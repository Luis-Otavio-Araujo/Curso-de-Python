import pygame
pygame.init()
pygame.mixer.music.load('musica021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
enter = input('Pressione enter para parar!')