import pygame
from functions import *
from constants import *

# Pause Page
# ? It is possible to combine this function with crash()?

def pause():
    message('Paused', lobsterL, -75)
    message('Press any key to continue', lobsterS, 0)

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
            elif event.type == pygame.KEYUP and event.key not in [pygame.K_a, pygame.K_d, pygame.K_LEFT, pygame.K_RIGHT]:
                return

            clock.tick(10)