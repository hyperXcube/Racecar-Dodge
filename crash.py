import pygame
from functions import *
from constants import *

# Crash Page
# ? Is it possible to combine this function with pause()

def crash(score):
    if score > shelf['record']:
        shelf['record'] = score
        message('New Record!!', lobsterL, -50, blue)
        pygame.draw.rect(display, white, (dispWD / 2, 3, dispWD / 2, 43))
        record = lobsterS.render('Record: ' + str(shelf['record']), True, blue)
        display.blit(record, record.get_rect(topright=(dispWD - 3, 3)))
    else:
        message('You Crashed', nosifer, -50, red)

    restartRect, homeRect, quitRect = buttons()

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if restartRect.collidepoint(mouse):
                    return crashButton.restart
                elif homeRect.collidepoint(mouse):
                    return crashButton.home
                elif quitRect.collidepoint(mouse):
                    end()
            elif event.type == pygame.KEYUP and event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                return crashButton.restart

            clock.tick(10)