import pygame
from functions import *
from constants import *

def crash(score, carChange):
    if score > shelf['record']:
        shelf['record'] = score
        message('New Record!!', lobsterL, -50, blue)
        pygame.draw.rect(display, white, (dispWD / 2, 3, dispWD / 2, 43))
        record = lobsterS.render('Record: ' + str(shelf['record']), True, blue)
        display.blit(record, record.get_rect(topright=(dispWD - 3, 3)))
    else:
        message('You Crashed', nosifer, -50, red)

    restartRect = button('Restart', green, (dispWD / 4, dispHT * 3 / 4))
    homeRect = button('Back to home', blue, (dispWD / 2, dispHT * 3 / 4), 200)
    quitRect = button('Quit', red, (dispWD * 3 / 4, dispHT * 3 / 4))

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
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if restartRect.collidepoint(mouse):
                    return crashButton.restart, carChange
                elif homeRect.collidepoint(mouse):
                    return crashButton.home, carChange
                elif quitRect.collidepoint(mouse):
                    end()
            elif event.type == pygame.KEYUP and event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                return crashButton.restart, carChange

            clock.tick(10)