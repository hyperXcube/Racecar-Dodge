import pygame, shelve
from settings import settings
from main import main
from functions import message, end
from constants import *

# Start Page

def start():
    display.fill(white)

    message('Racecar Dodge', lobsterL, -75)
    message('By Shaunak Warty', lobsterS, 0)
    message('Press any key to start', lobsterS, 50)

    gear = pygame.image.load(r'Images\gear.png')
    gearRect = gear.get_rect(topright=(dispWD - 3, 3))
    display.blit(gear, gearRect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.KEYUP:
                main()
                start()
            elif event.type ==  pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if gearRect.collidepoint(mouse):
                    settings()
                    start()

        clock.tick(10)

if 'record' not in shelf.keys():
    shelf['record'] = 0
    shelf['rectColor'] = black

start()