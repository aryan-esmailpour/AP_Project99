import pygame, sys, time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello')

pygame.mixer.music.load("/home/aryan/Desktop/APProject/AP_Project99/songs/Track 1.wav")
pygame.mixer.music.play()


while True: # Main Loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
