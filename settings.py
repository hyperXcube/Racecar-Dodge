import pygame
from functions import *
from constants import *

# settings page
def settings():
    colorRects = {}

    back = lobsterS.render('Back', True, black)
    backRect = back.get_rect(topleft = (5, 3))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type ==  pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if backRect.collidepoint(mouse):
                    return
                for color in colorRects.keys():
                    if colorRects[color].collidepoint(mouse):
                        shelf['rectColor'] = color

        display.fill(white)

        display.blit(back, backRect)
        display.blit(oswald.render('Change obstacle color:', True, black), (5, 75))  

        for i, color in enumerate(rectColors):
            pos = (dispWD - len(rectColors) * 100) / (len(rectColors) + 1) * (i + 1) + i * 100
            colorRects[color] = pygame.Rect(pos, 150, 100, 100)
            if shelf['rectColor'] == color:
                pygame.draw.rect(display, green, (pos - 3, 147, 106, 106))
            pygame.draw.rect(display, color, (pos, 150, 100, 100))

        pygame.display.update()
        clock.tick(10)