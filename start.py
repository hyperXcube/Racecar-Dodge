import pygame, shelve
from settings import settings
from main import gameMain
from functions import *
from constants import *

pygame.init()

# start page
def gameStart(carChange):
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
            elif event.type == pygame.KEYDOWN:
                if event.key == shelf['controls'][0]:
                    carChange -= 3
                elif event.key == shelf['controls'][1]:
                    carChange += 3
            elif event.type == pygame.KEYUP:
                if event.key == shelf['controls'][0]:
                    carChange += 3
                elif event.key == shelf['controls'][1]:
                    carChange -= 3
                carChange = gameMain(carChange)
                gameStart(carChange)
            elif event.type ==  pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if gearRect.collidepoint(mouse):
                    settings(carChange)
                    gameStart(carChange)

        clock.tick(10)

if 'record' not in shelf.keys():
    shelf['record'] = 0
    shelf['rectColor'] = black
    shelf['controls'] = arrowCtrl
gameStart(0)