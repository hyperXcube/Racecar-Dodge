import pygame, shelve
from settings import settings
from main import gameMain
from functions import *
from constants import *

pygame.init()

# start page
def gameStart():
    display.fill(white)

    message('Racecar Dodge', lobsterL, -75)
    message('By Shaunak Warty', lobsterS, 0)
    message('Press any key to start', lobsterS, 50)

    gear = pygame.image.load(r'Images\gear.png')
    gearRect = gear.get_rect(topright = (dispWD - 3, 3))
    display.blit(gear, gearRect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.KEYUP:
                gameMain()
                gameStart()
            elif event.type ==  pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if gearRect.collidepoint(mouse):
                    settings()
                    gameStart()

        clock.tick(10)

if 'record' not in shelf.keys():
    shelf['record'] = 0
    shelf['rectColor'] = black

gameStart()