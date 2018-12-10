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
                if event.key == pygame.K_LEFT:
                    carChange -= 4
                elif event.key == pygame.K_RIGHT:
                    carChange += 4
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    carChange += 4
                elif event.key == pygame.K_RIGHT:
                    carChange -= 4
                carChange = gameMain(carChange)
                gameStart(carChange)
            elif event.type ==  pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if gearRect.collidepoint(mouse):
                    carChange = settings(carChange)
                    gameStart(carChange)

        clock.tick(10)

gameStart(0)